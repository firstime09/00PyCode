import fungsi, glob, os, math, numexpr, datetime
import numpy as np
from datetime import datetime, date
from fungsi import build_data
from osgeo import gdal

path_f = 'Forest2020/M_8_1/*.txt' #---- read folder
glob_f = glob.glob(path_f)
data = open(glob_f[1])


# print(data1)

path = 'Forest2020/M_8_1/'
raster_list= glob.glob(path+ '*.TIF')
read=[]

data1 = build_data(data)

for i in raster_list:
    band = gdal.Open(i)
    read.append(band.GetRasterBand(1).ReadAsArray().astype(float))
filename=[]
for a in [os.path.basename(x) for x in glob.glob(path + '*.TIF')]:
    p=os.path.splitext(a)[0]
    filename.append(p)
my_dict= dict(zip(filename, read))

#Load data raster aspect & slope
pathname='Forest2020/123064/'
raster_list_dem=glob.glob(pathname+'*.TIF')
filename_dem=[]
for b in [os.path.basename(z) for z in glob.glob(pathname+'*.TIF')]:
    c=os.path.splitext(b)[0]
    filename_dem.append(c)

read2=[]
for d in raster_list_dem:
    band2=gdal.Open(d)
    read2.append(band2.GetRasterBand(1).ReadAsArray())
dem_dict= dict(zip(filename_dem, read2))