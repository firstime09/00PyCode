#----- 01PyCODE DATE: 07/11-2018
import FORESTS2020, os, gdal, glob, math
import numpy as np
from osgeo import gdal

# readPath = FORESTS2020.allFunc

# path = 'F:/PyFORESTS2020/#00Data/FORESTS2020'
# RPath = readPath.readFolder(path)
# print(RPath)

builData = FORESTS2020.allFunc
yearDate = FORESTS2020.allFunc
zoneDate = FORESTS2020.allFunc
hourHit = FORESTS2020.allFunc
secnHit = FORESTS2020.allFunc
dayHit = FORESTS2020.allFunc
leapHit = FORESTS2020.allFunc
cosAngle = FORESTS2020.allFunc
sinAngle = FORESTS2020.allFunc
sunAngle = FORESTS2020.allFunc
gammaHit = FORESTS2020.allFunc

path_f = 'F:/PyFORESTS2020/#00Data/FORESTS2020/M_8_1/*.txt'
glob_f = glob.glob(path_f)
f = open(glob_f[1])

data = builData.build_data(f) # 01
# print(data)

print("Load Data Raster....")
# Load data raster
path = 'F:/PyFORESTS2020/#00Data/FORESTS2020/M_8_1/'
raster_list = glob.glob(path+ '*.TIF')
read = []
for i in raster_list:
    band = gdal.Open(i)
    read.append(band.GetRasterBand(1).ReadAsArray().astype(float))
filename = []
for a in [os.path.basename(x) for x in glob.glob(path + '*.TIF')]:
    p = os.path.splitext(a)[0]
    filename.append(p)
my_dict = dict(zip(filename, read))

#Load data raster aspect & slope
pathname = 'F:/PyFORESTS2020/#00Data/FORESTS2020/M_8_1'
raster_list_dem = glob.glob(pathname + filename[0][10:16] + '/*.TIF')
filename_dem = []
for b in [os.path.basename(z) for z in glob.glob(pathname + filename[0][10:16] + '/*.TIF')]:
    c = os.path.splitext(b)[0]
    filename_dem.append(c)

read2 = []
for d in raster_list_dem:
    band2 = gdal.Open(d)
    read2.append(band2.GetRasterBand(1).ReadAsArray())
dem_dict = dict(zip(filename_dem, read2))

yDate = yearDate.year_date(data) # 02 year date
s = int(filename[0][10:16])
zZone = zoneDate.zone(s) # 03 time zone WIB, WIT or WITA
hHit = hourHit.hour(yDate, zZone) # 04 hour from the data
sHit = secnHit.second(yDate) # 05 second from the data
dHit = dayHit.day(yDate) # 06
leHit = leapHit.leap(yDate) # 07 Hit leap on the date
csHit = cosAngle.cos(30) # 08
snHit = cosAngle.sin(60) # 09
gmHit = gammaHit.hitGama(leHit, dHit, hHit, yDate, sHit) # 10
sunHit = sunAngle.sundecAngle(gmHit, snHit, csHit)

# print(yDate, '...', 'Zone Area:', zZone)
# print(hHit,'H',':',sHit,'S')
# print('Day:',dHit, 'Leap:',leHit)
print('Gamma Value:',gmHit, 'and' ,'Sun Angle:',sunHit)