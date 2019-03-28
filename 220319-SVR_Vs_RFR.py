from __future__ import print_function, division
from osgeo import gdal, gdal_array

gdal.UseExceptions()
gdal.AllRegister()

path_1 = ''
img_load = gdal.Open(path_1 + '.', gdal.GA_ReadOnly)