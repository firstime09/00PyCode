from __future__ import print_function, division
from osgeo import gdal, gdal_array
from sklearn.svm import SVR
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt
import openpyxl, numpy as np
import glob, pandas as pd
from Modul_ML.F17122018ML import F2020ML
from sklearn.model_selection import train_test_split
from Modul_Topo.F2020_RASTER import Raster_Func

gdal.UseExceptions()
gdal.AllRegister()

path_1 = r"D:\TIFF DATA\SUMATERA\GEE_WA_SUMSEL\Data Latihan"
load_stack_data = Raster_Func.stack_data(Raster_Func, input_path=path_1, name="_Data_Latihan")

# AOI_1 = gdal.Open(load_stack_data)
AOI_2 = load_stack_data.GetRasterBand(1).ReadAsArray()
AOI = AOI_2 > 0

# img_ds = gdal.Open(load_stack_data, gdal.GA_ReadOnly)
img = np.zeros((load_stack_data.RasterYSize, load_stack_data.RasterXSize, load_stack_data.RasterCount),
               gdal_array.GDALTypeCodeToNumericTypeCode(load_stack_data.GetRasterBand(1).DataType))
# print(img)
for b in range(img.shape[2]):
    img[:, :, b] = load_stack_data.GetRasterBand(b + 1).ReadAsArray()

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

## Load Dataframe for test the model
path_load = r"D:\TIFF DATA\SUMATERA\GEE_WA_SUMSEL\Data Latihan\L8_SMT_1_6_SEBELUM"
load_df = pd.read_excel(path_load + '/WA_Line_14_15_Sebelum_SMT_Balance.xlsx')
select_col_test = ['Band_2', 'Band_3', 'Band_4', 'Band_5', 'Band_6', 'Band_7']
select_row_test = 'frci5m'
dfx_test = pd.DataFrame(load_df, columns=select_col_test)
dfy_test = np.asarray(load_df[select_row_test])
y_pred_test = clfSVR_Model.predict(dfx_test)

# y_pred_df = y_pred.ravel(X_test)
# y_test_df = y_test.ravel()
df1 = pd.DataFrame({"y1": dfy_test})
df2 = pd.DataFrame({"y2": y_pred_test})
df_model = pd.concat([df1, df2], axis=1)

df_model.to_excel(path_load + "/test_model.xlsx")
model_rmse = F2020ML.F2020_RMSE(dfy_test, y_pred_test)
## Prediction model with data image
new_shape = (img.shape[0] * img.shape[1], img.shape[2])
img_as_array = img[:, :, :6].reshape (new_shape)
print('Reshaped from {o} to {n}'.format(o=img.shape, n=img_as_array.shape))

pred_model2data = clfSVR_Model.predict(img_as_array)
pred_model2data = pred_model2data.reshape(img[:, :, 0].shape)
pred_model2data[pred_model2data < 0] = 0.01
final_pred = pred_model2data * AOI

# out_path = path_1
# test = r"D:\TIFF DATA\SUMATERA\GEE_WA_SUMSEL\SUMSEL 1\L8_SMT_1_6_SESUDAHL8_SMT_Sesudah.tif"
# Raster_Func.saved_data_TIF(out_path, final_pred, name='_SVR_Data_', ras=test)

print(best_parm, 'Acc Model :', Acc_Model, '++++++', 'RMSE Model :', RMSE_Model)