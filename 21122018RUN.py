## Run Modul_ML and Modul_TOPO
import pandas as pd
import numpy as np
from Modul_Topo import FTEST01
from Modul_Topo.FORESTS2020 import allFunc
from Modul_ML.F17122018ML import F2020ML

# path = 'C:/Users/user/Dropbox/FORESTS2020/00AllData/Dataframe Sumatra/'
path = 'D:/GitHub/GitTesis/SVR/R export/'
dfxlx = pd.read_csv(path + '200219_DbscanSamp_1.5_5.csv')
column = ['Band_2', 'Band_3', 'Band_4', 'Band_5', 'Band_6', 'Band_7', 'DEM', 'ASPECT_R', 'SLOPE_R']
# column = ['PC1', 'PC2', 'PC3', 'PC4', 'PC5', 'PC6']
target = 'frci'
# target = 'dfy'
dfX = pd.DataFrame(dfxlx, columns=column)
dfY = np.asarray(dfxlx[target])

# dfcsv = pd.read_csv('C:/Users/user/Documents/R/Latihan LiDAR/R-Scripts/Latihan01/Cidanau_New_DF.csv')
# # dfx = dfcsv.iloc[:, :2]
# dfy = dfcsv.

# Check SVR and RFR parameters
print(dfxlx.head())
print('Values SVR: ', F2020ML.F2020_SVR(dfX, dfY, 0.3, 4))
print('Values RFR: ', F2020ML.F2020_RFR(dfX, dfY, 0.3, 4))
# print(F2020ML.plot_data(dfX, dfY))
