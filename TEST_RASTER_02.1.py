from __future__ import print_function, division
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from Modul_ML.F17122018ML import F2020ML
from Modul_Topo.F2020_RASTER import Raster_Func
from osgeo import gdal, gdal_array

gdal.UseExceptions()
gdal.AllRegister()

## Load Data Raster TIFF
path_raster = r"D:\TIFF DATA\SUMATERA\GEE_WA_SUMSEL\TST1_L8_SMT_SELATAN\SPLIT DATA TST1_L8"
load_stack_data = Raster_Func.stack_data(Raster_Func, input_path=path_raster, name="_Data_TST1")
AOI_2 = load_stack_data.GetRasterBand(1).ReadAsArray()
AOI = AOI_2 > 0
img = np.zeros((load_stack_data.RasterYSize, load_stack_data.RasterXSize, load_stack_data.RasterCount),
               gdal_array.GDALTypeCodeToNumericTypeCode(load_stack_data.GetRasterBand(1).DataType))
for b in range(img.shape[2]):
    img[:, :, b] = load_stack_data.GetRasterBand(b + 1).ReadAsArray()

plt.imshow(img[:, :, 4], cmap=plt.get_cmap('terrain'))
plt.title('DATA LandSat')

## Load Dataframe for make the model
path_train_DF = r"D:\00RCode\Result\Data Sumatera\Data Sumatera No_Normalize"
loadFile = pd.read_excel(path_train_DF + '/Cidanau_Join_LINE6_61.18.xlsx')
select_col = ['Band_2', 'Band_3', 'Band_4', 'Band_5', 'Band_6', 'Band_7']
select_row = 'frci'
dfx = pd.DataFrame(loadFile, columns=select_col)
dfy = np.asarray(loadFile[select_row])
##
clfSVR_train_model = F2020ML.SVR_Model(dfx, dfy, test_size=0.3, r_state=5)
print(clfSVR_train_model)

## Load Dataframe for test the model --- 1
path_test_DF = r"D:\TIFF DATA\F2020 All Data\SUMSEL\MALTA\Sebelum"
load_df = pd.read_excel(path_test_DF + '/SEBELUM_LINE_1_2_SUMSEL_BALANCE.xlsx')
select_col_test = ['Band_2', 'Band_3', 'Band_4', 'Band_5', 'Band_6', 'Band_7']
select_row_test = 'frci5m'
dfx_data = pd.DataFrame(load_df, columns=select_col_test)
dfy_data = np.asarray(load_df[select_row_test])

## Prediction data from model --- 2
dfy_pred = clfSVR_train_model.predict(dfx_data)
Model_RMSE = F2020ML.F2020_RMSE(dfy_data, dfy_pred)
print(Model_RMSE)
## Save Prediction data --- 3
df1 = pd.DataFrame({"Aktual": dfy_data})
df2 = pd.DataFrame({"Prediksi": dfy_pred})
df_model = pd.concat([df1, df2], axis=1)
df_model.to_excel(path_test_DF + "/SEBELUM_LINE_1_2_HASIL.xlsx")

## Prediction model with data image
new_shape = (img.shape[0] * img.shape[1], img.shape[2])
img_as_array = img[:, :, :6].reshape (new_shape)
print('Reshaped from {o} to {n}'.format(o=img.shape, n=img_as_array.shape))

pred_model2data = clfSVR_train_model.predict(img_as_array)
pred_model2data = pred_model2data.reshape(img[:, :, 0].shape)
pred_model2data[pred_model2data < 0] = 0.01
final_pred = pred_model2data * AOI

out_path = path_raster
stack_data = r"D:\TIFF DATA\SUMATERA\GEE_WA_SUMSEL\TST1_L8_SMT_SELATAN\SPLIT DATA TST1_L8_Data_TST1.tif"
Raster_Func.saved_data_TIF(out_path, final_pred, name='_SVR', ras=stack_data)
# print(best_parm, 'Acc Model :', Acc_Model, '++++++', 'RMSE Model :', RMSE_Model)