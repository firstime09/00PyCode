from __future__ import print_function, division
from sklearn.svm import SVR
from osgeo import gdal, gdal_array
from Modul_ML.F17122018ML import F2020ML
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

gdal.UseExceptions()
gdal.AllRegister()
path1 = 'D:/00PyCode/00AllData/Test_Data_08032019/'
img_ds = gdal.Open(path1 + 'layerstack.TIF', gdal.GA_ReadOnly)
# roi_ds = gdal.Open('D:/00PyCode/00AllData/Test_Data_08032019/training/training.TIF', gdal.GA_ReadOnly)

img = np.zeros((img_ds.RasterYSize, img_ds.RasterXSize, img_ds.RasterCount),
               gdal_array.GDALTypeCodeToNumericTypeCode(img_ds.GetRasterBand(1).DataType))

new_shape = (img.shape[0] * img.shape[1], img.shape[2])
new_as_array = img[:, :, :6].reshape(new_shape)

print(img.shape)
print(new_shape)
print(new_as_array)