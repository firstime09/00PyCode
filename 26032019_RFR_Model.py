from __future__ import print_function, division
from osgeo import gdal, gdal_array
from sklearn.ensemble import RandomForestRegressor
from sklearn.tree import export_graphviz
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt
import pydot, os
import numpy as np
import pandas as pd
from IPython.display import Image
from subprocess import call
from Modul_ML.F17122018ML import F2020ML
from sklearn.model_selection import train_test_split

def saved_data_TIF(in_path1, out_path1, pred_model, name):
    ## Make data prediction to TIF file
    saved_data = (name + "_Data_FRCI.TIF")
    output_path = (out_path1 + saved_data)
    raster = in_path1 + 'Cidanau_Stack_150319.tiff'
    in_path = gdal.Open(raster)
    in_array = pred_model
    ## global proj, geotrans, row, col
    proj = in_path.GetProjection()
    geotrans = in_path.GetGeoTransform()
    row = in_path.RasterYSize
    col = in_path.RasterXSize
    driver = gdal.GetDriverByName("GTiff")
    outdata = driver.Create(output_path, col, row, 1, gdal.GDT_CFloat64)
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

## Load data citra Landsat
path1 = 'D:/GitHub/GitTesis/TIF RAW/'
img_ds = gdal.Open(path1 + 'Cidanau_Stack_150319.tiff', gdal.GA_ReadOnly)

img = np.zeros((img_ds.RasterYSize, img_ds.RasterXSize, img_ds.RasterCount),
               gdal_array.GDALTypeCodeToNumericTypeCode(img_ds.GetRasterBand(1).DataType))
# print(img)
for b in range(img.shape[2]):
    img[:, :, b] = img_ds.GetRasterBand(b + 1).ReadAsArray()
# roi = roi_ds.GetRasterBand(1).ReadAsArray().astype(np.uint8)

# plt.subplot(121)
# plt.imshow(img[:, :, 4], cmap = plt.cm.Greys_r)
# plt.title('DATA LandSat')

## Load Dataframe for make the model
path2 = 'D:/00RCode/Result/01042019_JOIN_DF_LINE_1.2/'
loadFile = pd.read_excel(path2 + 'CIDANAU_LINE_1_2_SUMATERA_77_14.xlsx')
select_col = ['Band_2', 'Band_3', 'Band_4', 'Band_5', 'Band_6', 'Band_7']
select_row = 'frci'

dfx = pd.DataFrame(loadFile, columns=select_col)
dfy = np.asarray(loadFile[select_row])

X_train, X_test, y_train, y_test = train_test_split(dfx, dfy, test_size=0.3, random_state=10)
# sc = MinMaxScaler()
# X_train = sc.fit_transform(X_train)
# X_test = sc.transform(X_test)

best_score = 0
for n_estimate in [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]:
    for r_state in [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]:
        clfRFR = RandomForestRegressor(n_estimators=n_estimate, random_state=r_state)
        clfRFR.fit(X_train, y_train)
        score = clfRFR.score(X_test, y_test)
        if score > best_score:
            best_score = score
            best_rstate = r_state
            best_estimate = n_estimate
            best_parm = {'Estimators':best_estimate, 'Random State':best_rstate}

clfRFR_Model = RandomForestRegressor(n_estimators=best_estimate, random_state=best_rstate)
clfRFR_Model.fit(X_train, y_train)
Acc_Model = clfRFR_Model.score(X_test, y_test)
y_pred = clfRFR_Model.predict(X_test)
RMSE_Model = F2020ML.F2020_RMSE(y_test, y_pred)

## Pull out one tree from the model
# tree = clfRFR_Model.estimators_[5]
# export_graphviz(tree, out_file='tree.dot')
# # call(['dot', '-Tpng', 'tree.dot', '-o', 'tree.png', '-Gdpi=600'])
# # Image(filename='tree.png')
# (graph, ) = pydot.graph_from_dot_file('tree.dot')
# graph.write_png('tree.png')

## Prediction model with data image
new_shape = (img.shape[0] * img.shape[1], img.shape[2])
img_as_array = img[:, :, :6].reshape(new_shape)
print('Reshaped from {o} to {n}'.format(o=img.shape, n=img_as_array.shape))

pred_model2data = clfRFR_Model.predict(img_as_array)
pred_model2data = pred_model2data.reshape(img[:, :, 0].shape)

path3 = 'D:/00RCode/Result/01042019_JOIN_DF_LINE_1.2/TIff File/'
saved_data_TIF(path1, path3, pred_model2data, name='02042019_RFR_03')

print(best_parm, 'Acc Model :', Acc_Model, '++++++', 'RMSE Model :', RMSE_Model)

# plt.imshow(class_prediction, interpolation='none')
# plt.show()