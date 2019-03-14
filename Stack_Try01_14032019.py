import glob
import numpy as np
import matplotlib.pyplot as plt
from osgeo import gdal, gdal_array
from skimage.external import tifffile

gdal.UseExceptions()
gdal.AllRegister()

path_save = 'D:/00AllData/123064/'
with tifffile.TiffWriter(path_save + 'Stack_Data.tif') as stack:
    for filename in glob.glob('D:/00AllData/123064/*.TIF'):
        stack.save(tifffile.imread(filename), photometric='minisblack')

load_stack_data = gdal.Open(path_save + 'Stack_Data.tif', gdal.GA_ReadOnly)

img = np.zeros((load_stack_data.RasterYSize, load_stack_data.RasterXSize, load_stack_data.RasterCount),
               gdal_array.GDALTypeCodeToNumericTypeCode(load_stack_data.GetRasterBand(1).DataType))
# print(img)
for b in range(img.shape[2]):
    img[:, :, b] = load_stack_data.GetRasterBand(b + 1).ReadAsArray()
# roi = roi_ds.GetRasterBand(1).ReadAsArray().astype(np.uint8)

# plt.subplot(121)
plt.imshow(img[:, :, 4], cmap = plt.cm.Greys_r)
plt.title('DATA LandSat')

# plt.imshow(load_stack_data, interpolation='none')
plt.show()