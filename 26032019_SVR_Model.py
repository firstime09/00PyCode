from __future__ import print_function, division
from osgeo import gdal, gdal_array
from sklearn.svm import SVR
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt
import numpy as np
import glob, pandas as pd
from Modul_ML.F17122018ML import F2020ML
from sklearn.model_selection import train_test_split

def saved_data_TIF(out_path1, pred_model, name, ras):
    ## Make data prediction to TIF file
    saved_data = (name + "_Data_FRCI.TIF")
    output_path = (out_path1 + saved_data)
    # raster = in_path1 + '/CIDANAU_STACK_13052019.tif'
    raster = ras
    in_path = gdal.Open(raster)
    in_array = pred_model
    ## global proj, geotrans, row, col
    proj = in_path.GetProjection()
    geotrans = in_path.GetGeoTransform()
    row = in_path.RasterYSize
    col = in_path.RasterXSize
    driver = gdal.GetDriverByName("GTiff")
    outdata = driver.Create(output_path, col, row, 1, gdal.GDT_Float32)
    outband = outdata.GetRasterBand(1)
    outband.SetNoDataValue(-9999)
    outband.WriteArray(in_array)
    outdata.SetGeoTransform(geotrans)  # Georeference the image
    outdata.SetProjection(proj)  # Write projection information
    outdata.FlushCache()
    outdata = None
    return outdata

gdal.UseExceptions()
gdal.AllRegister()


#### stack layer data
path_layer = r"D:\TIFF DATA\New DataFrame\Cidanau 13052019\TIFF FILE\Erdas Stack Cidanau Sesudah"
file_layer = glob.glob(path_layer + "/*.tif")

file_vrt = path_layer + "/stacked.vrt"
file_tif = path_layer + "/CIDANAU_STACK_Sesudah_15052019_1.tif"
vrt = gdal.BuildVRT(file_vrt, file_layer, separate=True)
stack_layer = gdal.Translate(file_tif, vrt)


#####
AOI_1 = gdal.Open(file_tif)
AOI_2 = AOI_1.GetRasterBand(1).ReadAsArray()
AOI = AOI_2 > 0

## Load data citra Landsat
# path1 = r'D:\GitFolder1611\GitTesis\TIF RAW\stack'
# img_ds = gdal.Open(path1 + '/cidanau_stack.tif', gdal.GA_ReadOnly)
#
# img = np.zeros((img_ds.RasterYSize, img_ds.RasterXSize, img_ds.RasterCount),
#                gdal_array.GDALTypeCodeToNumericTypeCode(img_ds.GetRasterBand(1).DataType))


img_ds = gdal.Open(file_tif, gdal.GA_ReadOnly)
img = np.zeros((img_ds.RasterYSize, img_ds.RasterXSize, img_ds.RasterCount),
               gdal_array.GDALTypeCodeToNumericTypeCode(img_ds.GetRasterBand(1).DataType))
# print(img)
for b in range(img.shape[2]):
    img[:, :, b] = img_ds.GetRasterBand(b + 1).ReadAsArray()
# roi = roi_ds.GetRasterBand(1).ReadAsArray().astype(np.uint8)

# plt.subplot(121)
# plt.imshow(img[:, :, 4], cmap = plt.cm.Greys_r)
# plt.title('DATA LandSat')
plt.imshow(img[:, :, 4], cmap = plt.cm.Greys_r)
plt.title('DATA LandSat')

## Load Dataframe for make the model
path2 = r"D:\00RCode\Result\Data Sumatera\Data Sumatera No_Normalize"
loadFile = pd.read_excel(path2 + '/Cidanau_Join_LINE6_61.18.xlsx')
select_col = ['Band_2', 'Band_3', 'Band_4', 'Band_5', 'Band_6', 'Band_7']
select_row = 'frci'

dfx = pd.DataFrame(loadFile, columns=select_col)
dfy = np.asarray(loadFile[select_row])

X_train, X_test, y_train, y_test = train_test_split(dfx, dfy, test_size=0.3, random_state=5)
# sc = MinMaxScaler()
# X_train = sc.fit_transform(X_train)
# X_test = sc.transform(X_test)

best_score = 0
for C in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    for gamma in [0.01, 0.1, 0.2, 0.3, 0.4, 0.5, 1]:
        for epsilon in [0.001, 0.01, 0.1, 0.2, 0.3, 0.4, 0.5]:
            clfSVR = SVR(kernel='rbf', C=C, gamma=gamma, epsilon=epsilon)
            clfSVR.fit(X_train, y_train)
            score = clfSVR.score(X_test, y_test)
            if score > best_score:
                best_score = score
                best_C = C
                best_gamma = gamma
                best_epsilon = epsilon
                best_parm = {'C':best_C, 'Gamma':best_gamma, 'Epsilon':best_epsilon}

clfSVR_Model = SVR(kernel='rbf', C=best_C, gamma=best_gamma, epsilon=best_epsilon)
clfSVR_Model.fit(X_train, y_train)
Acc_Model = clfSVR_Model.score(X_test, y_test)
y_pred = clfSVR_Model.predict(X_test)
RMSE_Model = F2020ML.F2020_RMSE(y_test, y_pred)

## Prediction model with data image
new_shape = (img.shape[0] * img.shape[1], img.shape[2])
img_as_array = img[:, :, :6].reshape(new_shape)
print('Reshaped from {o} to {n}'.format(o=img.shape, n=img_as_array.shape))

pred_model2data = clfSVR_Model.predict(img_as_array)
pred_model2data = pred_model2data.reshape(img[:, :, 0].shape)
pred_model2data[pred_model2data < 0] = 0.01
final_pred = pred_model2data * AOI

# F:\All Data Forests2020\Path112Row56 Manado\TOA MANADO
out_path = r"D:\TIFF DATA\New DataFrame\Cidanau 13052019\TIFF FILE\Erdas Stack Cidanau Sesudah"
saved_data_TIF(out_path, final_pred, name='SVR_Data_CIDANAU', ras=file_tif)

print(best_parm, 'Acc Model :', Acc_Model, '++++++', 'RMSE Model :', RMSE_Model)
# plt.imshow(class_prediction, interpolation='none')
# plt.show()