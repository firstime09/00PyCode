from __future__ import print_function, division
import sys, glob
# sys.path.append('D:\\FORESTS2020\\GITHUB\\Plugin\\GitTesis\\21122018')
# sys.path.append('C:\\Program Files\\GDAL')
from sklearn.svm import SVR
from osgeo import gdal, gdal_array
from Modul_ML.F17122018ML import F2020ML
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import glob, numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#### stack layer data
path_layer = r"D:\TIFF DATA\New DataFrame\Cidanau 13052019\TIFF FILE\Erdas Stack Cidanau"
file_layer = glob.glob(path_layer + "/*.tif")
# system('gdal_merge -o cidanau_stack.tif {fileraster}'.format(fileraster=file_layer))
# gm.main(['', '-o', 'cidanau_stack.tif', '{fileraster}'.format(fileraster=file_layer)])
file_vrt = path_layer + "/stacked.vrt"
file_tif = path_layer + "/CIDANAU_STACK_13052019.tif"
vrt = gdal.BuildVRT(file_vrt, file_layer, separate=True)
stack_layer = gdal.Translate(file_tif, vrt)


#####
AOI_1 = gdal.Open(file_tif)
AOI_2 = AOI_1.GetRasterBand(1).ReadAsArray()
AOI = AOI_2 > 0


img_ds = gdal.Open(file_tif, gdal.GA_ReadOnly)
img = np.zeros((img_ds.RasterYSize, img_ds.RasterXSize, img_ds.RasterCount),
               gdal_array.GDALTypeCodeToNumericTypeCode(img_ds.GetRasterBand(1).DataType))
# print(img)
for b in range(img.shape[2]):
    img[:, :, b] = img_ds.GetRasterBand(b + 1).ReadAsArray()
# roi = roi_ds.GetRasterBand(1).ReadAsArray().astype(np.uint8)

# plt.subplot(121)
plt.imshow(img[:, :, 4], cmap = plt.cm.Greys_r)
plt.title('DATA LandSat')

# path = r"F:\All Data Forests2020\Path104Row61 Serui\TOA Serui"
# b2 = gdal.Open(path + "/B2.TIF")
# b3 = gdal.Open(path + "/B3.TIF")
# b4 = gdal.Open(path + "/B4.TIF")
# b5 = gdal.Open(path + "/B5.TIF")
# b6 = gdal.Open(path + "/B6.TIF")
# b7 = gdal.Open(path + "/B7.TIF")
#
# aray2 = b2.ReadAsArray()
# aray3 = b3.ReadAsArray()
# aray4 = b4.ReadAsArray()
# aray5 = b5.ReadAsArray()
# aray6 = b6.ReadAsArray()
# aray7 = b7.ReadAsArray()
# stacked = np.array([aray2, aray3, aray4, aray5, aray6, aray7])
# gdal_array.SaveArray(stacked, path + "/SERUI_Stack_080519.tiff", "GTiff")

# def stack_data(path):
#     for data in glob.glob(path + "/*.tif"):
#         load_data = gdal.Open(data)
#         aray_data = load_data.ReadAsArray()
#         stacked = np.array([aray_data])
#         saved = gdal_array.SaveArray(stacked, "Data_Stack.tiff", "GTiff")
#     return(saved)

# def read_data(data):
#     band = gdal.Open(data)
#     array_band = band.ReadAsArray()
#     stacked = np.array([array_band])
#     # saved_data = gdal_array.SaveArray(stacked, "Data_Stack.tiff", "GTiff")
#     return stacked
#
# for band_load in glob.glob('D:/GitFolder1611/GitTesis/TIF RAW/*.tif'):
#     run_data = read_data(band_load)
#     save_data = gdal_array.SaveArray(run_data, "Data_Stack.tiff", "GTiff")