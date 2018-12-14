import glob, gdal

# path_f = 'Forest2020/M_8_1/*.txt' #---- read folder
# glob_f = glob.glob(path_f)
# data = open(glob_f[1])

path = 'Forest2020/M_8_1/'
raster_list= glob.glob(path+ '*.TIF')
read=[]

def build_data(data):
    output = {}
    for line in data.readlines():
        if "=" in line:
            l = line.split("=")
            output[l[0].strip()] = l[1].strip()
    return output

def data_raster(data):
    for i in data.raster_list():
        band = gdal.Open(i)
        filename = read.append(band.GetRasterBand(1).ReadAsArray().astype(float))
        filename1 = []
    return filename1