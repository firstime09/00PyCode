import datetime, math, glob, csv, os, numexpr
from datetime import datetime, date
import numpy as np
from osgeo import gdal
from scipy.stats import linregress
#Load Metadata
path_f = r"F:\All Data Forests2020\Path112Row56 Manado\*.txt" #open file for reading
glob_f = glob.glob(path_f)
f = open(glob_f[1])
def build_data(f):
    output = {}
    for line in f.readlines():
        if "=" in line:
            l = line.split("=")
            output[l[0].strip()] = l[1].strip()
    return output
data = build_data(f)

#Load data raster
print ("Loading Data Raster...")
#Load data raster
path = r"F:\All Data Forests2020\Path112Row56 Manado"
raster_list = glob.glob(path + '/*.TIF')
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
pathname = 'D:/FORESTS2020/TRAINING/PyQgis/DATA/Landsat8/CIDANAU/GEO/FINAL/DEM/'
raster_list_dem = glob.glob(pathname+filename[0][10:16]+'/*.TIF')
filename_dem = []
for b in [os.path.basename(z) for z in glob.glob(pathname+filename[0][10:16]+'/*.TIF')]:
    c = os.path.splitext(b)[0]
    filename_dem.append(c)
read2 = []
for d in raster_list_dem:
    band2 = gdal.Open(d)
    read2.append(band2.GetRasterBand(1).ReadAsArray())
dem_dict = dict(zip(filename_dem, read2))

def year_date():
    year_file = data['DATE_ACQUIRED']
    date_file = data['SCENE_CENTER_TIME']
    date_file2 = date_file [1:16]
    all = year_file+" "+date_file2
    parsing = datetime.strptime(all, '%Y-%m-%d %H:%M:%S.%f')
    return parsing
dt = year_date()

WIT = [102061, 102062, 102063, 102064, 102065, 102066, 109058, 109059, 109060, 109061, 109062, 109063, 109064, 109065, 109066, 109067, 100062, 100063, 100064, 100065,
       100066, 107059, 107060, 107061, 107062, 107063, 107064, 107065, 107066, 105060, 105061, 105062, 105063, 105064, 105065, 103061, 103062, 103063, 103064, 110057,
       110058, 110059, 110060, 110061, 110062, 110063, 110064, 110065, 110066, 110067, 101061, 101062, 101063, 101064, 101065, 101066, 108060, 108061, 108062, 108063,
       108064, 108065, 108066, 106060, 106061, 106062, 106063, 106064, 106065, 106066, 104060, 104061, 104062, 104063, 104064, 104065, 111060, 111061, 111062]
WIB = [118060, 118061, 118062, 118063, 118064, 118065, 118066, 125059, 125060, 125061, 125062, 125063, 125064, 123057, 123058, 123059, 123060, 123061, 123062,
      123063, 123064, 123065, 130056, 130057, 130058, 130059, 121060, 121061, 121062, 121063, 121064, 121065, 128057, 128058, 128059, 128060, 128061, 119060,
      119061, 119062, 119063, 119064, 119065, 119066, 126059, 126060, 126061, 126062, 126063, 124058, 124059, 124060, 124061, 124062, 124063, 124064, 124065,
      131056, 131057, 131058, 122058, 122059, 122060, 122061, 122062, 122063, 122064, 122065, 129057, 129058, 129059, 129060, 120060, 120061, 120062, 120063,
      120064, 120065, 120066, 127058, 127059, 127060, 127061, 127062]
s = int(filename[0][10:16])

def zone():
    if s in WIB:
        k = int(7)
    elif s in WIT:
        k = int(9)
    else:
        k = int(8)
    return k

def hour():
    h = dt.hour+ zone()
    return h
def second():
    s = float(dt.microsecond)/1000000+dt.second
    return s
def leap():
    if (dt.year % 4) == 0:
        if (dt.year % 100) == 0:
            if (dt.year % 400) == 0:
               a = int(366)
            else:
                a = int(365)
        else:
            a = int(366)
    else:
        a = int(365)
    return a
def cos(x):
    cos = np.cos(np.deg2rad(x))
    return cos
def sin(x):
    sin = np.sin(np.deg2rad(x))
    return sin
def day():
    day_date = date(dt.year, dt.month, dt.day)
    sum_of_day = int(day_date.strftime('%j'))
    return sum_of_day
print ("Calculating Solar Position...")
gamma = ((2 * math.pi) / leap()) * ((day() - 1) + (((hour()+dt.minute/60+second()/3600) - 12) / 24) )# degree


#sun declination angle
decl = 0.006918 - 0.399912 * cos(gamma) + 0.070257 * sin(gamma) - 0.006758 * cos (2 * gamma)\
     + 0.000907 * sin (2 * gamma) - 0.002697 * cos (3 * gamma) + 0.00148 * sin (3 * gamma) #radians
decl_deg = (360 / (2 * math.pi)) * decl

#lat long value
# get columns and rows of your image from gdalinfo
# xoff, a, b, yoff, d, e = band.GetGeoTransform()
def pixel2coord(x, y):
    xoff, a, b, yoff, d, e = band.GetGeoTransform()
    xp = a * x + b * y + xoff
    yp = d * x + e * y + yoff
    return(xp, yp)
rows = read[0].shape[0]
colms = read[0].shape[1]
coordinate = []
for row in range(0, rows):
  for col in range(0, colms):
      coordinate.append(pixel2coord(col,row))
coor_2 = np.array(coordinate, dtype=float)
long = coor_2[:,0]
lat = coor_2[:,1]
long_n = long.reshape(rows,colms)
lat_n = lat.reshape(rows,colms)

#eqtime
eqtime = 229.18 * (0.000075 + 0.001868 * cos(gamma) - 0.032077 * sin(gamma) - 0.014615 * cos(2 * gamma) - 0.040849 * sin(2 * gamma))  # minutes
timeoff = eqtime - 4 * long_n + 60 * 7 #minutes
tst = hour() * 60 + dt.minute + second() / 60 + timeoff #minutes
ha = (tst /4)-180 #degree

#sun zenith angle
zenit1 = sin(lat_n)* sin(decl_deg) + cos (lat_n)* cos(decl_deg) * cos(ha)
zenit2 = np.arccos(zenit1) #radians
zenit_angle = np.rad2deg(zenit2)

#sun azimuth angle
theta1 = -1 * ((sin(lat_n)) * cos(zenit_angle)- sin(decl_deg)/(cos (lat_n) * sin (zenit_angle)))
theta2 = np.arccos(theta1) #radians
theta3 = np.rad2deg(theta2)#degree
azimuth_angle = 180 - theta3 #degrees

# mengambil data berdasarkan extent layer
rows = read[0].shape[0]
colms = read[0].shape[1]
AOI = read[5] >= 0
AOI_true = np.nonzero(AOI)
AOI_a_true = AOI_true[0]
AOI_b_true = AOI_true[1]
ASPECT = dem_dict['aspect'][AOI_a_true, AOI_b_true].reshape(rows, colms)
SLOPE = dem_dict['slope'][AOI_a_true, AOI_b_true].reshape(rows, colms)


# IC calculation
# delta=azimuth_angle - dem_dict['aspect']
delta = azimuth_angle - ASPECT
# delta=float(data['SUN_AZIMUTH'])- (dem_dict['aspect'])
# zenit_angle= 90 - float(data['SUN_ELEVATION'])
IC_1 = (cos(zenit_angle)* cos (SLOPE)) + (sin(zenit_angle) * sin (SLOPE) * cos(delta))#radians
IC_true = IC_1[AOI_a_true, AOI_b_true]
IC = IC_true.reshape(rows, colms)
#Reflectance convert from float to Uint 16bit, multipled by 44500
reflectance_band1 = (float(data['REFLECTANCE_MULT_BAND_1'])*my_dict[filename[0][:-2]+'B1']+float(data['REFLECTANCE_ADD_BAND_1']))/cos(zenit_angle)*44500
reflectance_band2 = (float(data['REFLECTANCE_MULT_BAND_2'])*my_dict[filename[0][:-2]+'B2']+float(data['REFLECTANCE_ADD_BAND_2']))/cos(zenit_angle)*44500
reflectance_band3 = (float(data['REFLECTANCE_MULT_BAND_3'])*my_dict[filename[0][:-2]+'B3']+float(data['REFLECTANCE_ADD_BAND_3']))/cos(zenit_angle) *44500
reflectance_band4 = (float(data['REFLECTANCE_MULT_BAND_4'])*my_dict[filename[0][:-2]+'B4']+float(data['REFLECTANCE_ADD_BAND_4']))/cos(zenit_angle) *44500
reflectance_band5 = (float(data['REFLECTANCE_MULT_BAND_5'])*my_dict[filename[0][:-2]+'B5']+float(data['REFLECTANCE_ADD_BAND_5']))/cos(zenit_angle) *44500
reflectance_band6 = (float(data['REFLECTANCE_MULT_BAND_6'])*my_dict[filename[0][:-2]+'B6']+float(data['REFLECTANCE_ADD_BAND_6']))/cos(zenit_angle) *44500
reflectance_band7 = (float(data['REFLECTANCE_MULT_BAND_7'])*my_dict[filename[0][:-2]+'B7']+float(data['REFLECTANCE_ADD_BAND_7']))/cos(zenit_angle) *44500
reflectance_band9 = (float(data['REFLECTANCE_MULT_BAND_9'])*my_dict[filename[0][:-2]+'B9']+float(data['REFLECTANCE_ADD_BAND_9']))/cos(zenit_angle) *44500
# reflectance_f= {filename[0][:-2]+'B1':reflectance_band1, filename[0][:-2]+'B2':reflectance_band2,filename[0][:-2]+'B3':reflectance_band3, filename[0][:-2]+'B4':reflectance_band4, filename[0][:-2]+'B5':reflectance_band5, filename[0][:-2]+'B6':reflectance_band6, filename[0][:-2]+'B7':reflectance_band7, filename[0][:-2]+'B9':reflectance_band9}
reflectance_f = {'B1':reflectance_band1, 'B2':reflectance_band2,'B3':reflectance_band3, 'B4':reflectance_band4, 'B5':reflectance_band5, 'B6':reflectance_band6, 'B7':reflectance_band7, 'B9':reflectance_band9}


# sample
NDVI = numexpr.evaluate("(reflectance_band5 - reflectance_band4) / (reflectance_band5 + reflectance_band4)")
slope_sample = dem_dict["slope"] >= 18
sample_ndvi = numexpr.evaluate("(NDVI >0.5) & (slope_sample == True)")
area_true = sample_ndvi.nonzero() #outputnya index row n col
a_true = area_true[0]
b_true = area_true[1]
#correction or Rotation Model
cos_zenith = cos(zenit_angle)
coba = []
temp = {}
IC_final = {}
Bheta = []
for y, value in sorted(reflectance_f.items()):
        val2 = reflectance_f[y]
        temp[y] = val2[a_true,b_true].ravel()
        IC_true = IC[a_true,b_true].ravel()
        slope = linregress(IC_true, temp[y])
        coba.append(slope[0])
        # print y
        IC_final[y] = reflectance_f[y]-(slope[0]*(IC-cos_zenith))
        print(y, slope[0])
#export auto
for item in IC_final:
    geo = band.GetGeoTransform()
    proj = band.GetProjection()
    shape = my_dict[filename[0][:-2]+'B1'].shape
    driver = gdal.GetDriverByName("GTiff")
    # dst_ds = driver.Create("D:/FORESTS2020/TRAINING/PyQgis/RESULT/REPORT/050918/" + filename[0][17:24]+"/"+item + "_topo.TIF", shape[1], shape[0], 1, gdal.GDT_Float32)
    dst_ds = driver.Create("D:/FORESTS2020/TRAINING/PyQgis/RESULT/REPORT/050918/Piksel/8/" + filename[0][10:25]+ item + "_topo.TIF", shape[1], shape[0], 1, gdal.GDT_Float32)
    dst_ds.SetGeoTransform(geo)
    dst_ds.SetProjection(proj)
    ds = dst_ds.GetRasterBand(1)
    ds.SetNoDataValue(-9999)
    ds.WriteArray(IC_final[item])
    dst_ds.FlushCache()
    dst_ds = None  # save, close""
#Report
# Matriks_true = np.zeros(read[4].shape)
#Area
rows = read[0].shape[0]
colms = read[0].shape[1]
AOI = read[5]> 0
AOI_true = np.nonzero(AOI)
AOI_a_true = AOI_true[0]
AOI_b_true = AOI_true[1]
# ASPECT=dem_dict['aspect'][AOI_a_true, AOI_b_true].reshape(rows, colms)
Slope_true = dem_dict['slope'][AOI_a_true, AOI_b_true]
Slope_true[Slope_true<0] = 0
IC_R = IC[AOI_a_true,AOI_b_true]
# Matriks_true[a_true,b_true]= dem_dict['slope'][a_true,b_true]
slope_sample = dem_dict['slope'][a_true, b_true]
IC_sample = IC[a_true, b_true]
piksel = int(rows*colms)
today = date.today()
today_par = datetime.strftime(today, '%Y-%m-%d')


# Report CSV
with open("D:/FORESTS2020/TRAINING/PyQgis/RESULT/REPORT/050918/Piksel/8/"+ filename[0][10:25]+ "_PIKSEL_REPORT.csv", 'wb') as csvfile:
    filewriter = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
    filewriter.writerow(['Tanggal', 'Kondisi Awan', 'Path/Row', 'Slope1_min', 'Slope1_max', 'Slope1_mean', 'Slope1_std',
                         'Slope2_min', 'Slope2_max', 'Slope2_mean', 'Slope2_std', 'IC1_min', 'IC1_max', 'IC1_mean',
                         'IC1_std', 'IC2_min', 'IC2_max', 'IC2_mean', 'IC2_std', 'Jml_piksel', 'Jml_Sampel', 'Bheta_B1','Bheta_B2', 'Bheta_B3', 'Bheta_B4', 'Bheta_B5', 'Bheta_B6', 'Bheta_B7', 'Bheta_B9'])
    filewriter.writerow([data['DATE_ACQUIRED'], data['CLOUD_COVER_LAND'], filename[0][10:16], Slope_true.min(),
                         Slope_true.max(), Slope_true.mean(), Slope_true.std(), slope_sample.min(), slope_sample.max(),
                         slope_sample.mean(), slope_sample.std(),
                         IC_R.min(), IC_R.max(), IC_R.mean(), IC_R.std(), IC_sample.min(), IC_sample.max(),
                         IC_sample.mean(), IC_sample.std(), piksel,
                         len(a_true), coba[0], coba[1], coba[2], coba[3], coba[4], coba[5], coba[6], coba[7]])
