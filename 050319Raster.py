import os, glob
import numpy as np
from osgeo import gdal

# path = 'C:/Users/user/Dropbox/FORESTS2020/00AllData/DATA/From Eci/landsat/LC80340322016189-SC20170128091153/crop/'
path = 'D:/00AllData/00 Data Load/Path112Row56 Manado/'
ds = glob.glob(os.path.join(path, '*.TIF'))
raster = [os.path.split(item)[1] for item in ds]
print(raster)

#--- Perform for averaging data
for i, file in enumerate(ds):
    dataset = gdal.Open(file)
    band = dataset.GetRasterBand(1)
    data = band.ReadAsArray()

    print(raster[i], "Mean: ", np.mean(data))