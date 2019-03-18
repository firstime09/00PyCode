from osgeo import gdal, gdal_array
import numpy as np
import glob

path = 'D:/GitFolder1611/GitTesis/TIF RAW'
b2 = gdal.Open(path + "Band 2.tif")
b3 = gdal.Open(path + "Band 3.tif")
b4 = gdal.Open(path + "Band 4.tif")
b5 = gdal.Open(path + "Band 5.tif")
b6 = gdal.Open(path + "Band 6.tif")
b7 = gdal.Open(path + "Band 7.tif")

aray2 = b2.ReadAsArray()
aray3 = b3.ReadAsArray()
aray4 = b4.ReadAsArray()
aray5 = b5.ReadAsArray()
aray6 = b6.ReadAsArray()
aray7 = b7.ReadAsArray()
stacked = np.array([aray2, aray3, aray4, aray5, aray6, aray7])
gdal_array.SaveArray(stacked, path + "Cidanau_Stack_150319.tiff", "GTiff")

# def stack_data(path):
#     for data in glob.glob(path + "/*.tif"):
#         load_data = gdal.Open(data)
#         aray_data = load_data.ReadAsArray()
#         stacked = np.array([aray_data])
#         saved = gdal_array.SaveArray(stacked, "Data_Stack.tiff", "GTiff")
#     return(saved)

def read_data(data):
    band = gdal.Open(data)
    array_band = band.ReadAsArray()
    stacked = np.array([array_band])
    # saved_data = gdal_array.SaveArray(stacked, "Data_Stack.tiff", "GTiff")
    return stacked

for band_load in glob.glob('D:/GitFolder1611/GitTesis/TIF RAW/*.tif'):
    run_data = read_data(band_load)
    save_data = gdal_array.SaveArray(run_data, "Data_Stack.tiff", "GTiff")