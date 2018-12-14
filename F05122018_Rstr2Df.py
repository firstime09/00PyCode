## Mengektrak data raster menjadi dataframe => raster to dataframe
import glob, gdal, os
import pandas as pd
from pandas import DataFrame, Series

print ("Loading Data Raster...")
## Load data raster
path = 'D:/GitHub/GitTesis/RAW DATA/'
raster_list = glob.glob(path+ '*.IMG')
read = []
# print(raster_list)
for i in raster_list:
    band = gdal.Open(i)
    read.append(band.GetRasterBand(1).ReadAsArray().astype(float))

print(filename)
filename =[]
for a in [os.path.basename(x) for x in glob.glob(path+ '*.IMG')]:
    p = os.path.splitext(a)[0]
    filename.append(p)
my_dict = dict(zip(filename, read))
print(my_dict)
ravel = []
data = []
for i in range(len(read)):
    ravel.append(read[i].ravel())
    # dataframe = pd.DataFrame({i:ravel[i]})
    dataframe = pd.DataFrame({i:ravel[i]})
    data.append(dataframe)
    # print (dataframe)

dfn = pd.concat([data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7]], axis=1)
# dfn.to_csv('test.csv', index=False)
dfn.to_excel('D:/Result/New_Data Train CIDANAU.xlsx', sheet_name='sheet1', index=False)
# band2R = read[1].ravel()
# band2 = pd.DataFrame({'B2':band2R})
## Make data raster in dataFrame
# index = ['Band1','Band2','Band3','Band4','Band5','Band6','Band7','Band9']
# df = DataFrame(my_dict, index)
# print(df)