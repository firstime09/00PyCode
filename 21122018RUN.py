## Run Modul_ML and Modul_TOPO
import pandas as pd
import numpy as np
from Modul_Topo import F2020_RASTER
from Modul_Topo.FORESTS2020 import allFunc
from Modul_ML.F17122018ML import F2020ML

# path = 'C:/Users/user/Dropbox/FORESTS2020/00AllData/Dataframe Sumatra/'
path = r"D:\Bang Wim\SET_SAMPLES"
dfxlx = pd.read_excel(path + '/All_Data_Set_Bg.Wim.xlsx')
column = ['b2', 'b3', 'b4', 'b5', 'b6', 'b7']
# column = ['Band_2', 'Band_3', 'Band_4', 'Band_5', 'Band_6', 'Band_7']
# column = ['PC1', 'PC2']
target = 'FRCI'
# target = 'dfy'
dfX = pd.DataFrame(dfxlx, columns=column)
dfY = np.asarray(dfxlx[target])

# Check SVR and RFR parameters
print(dfxlx.head())
print('Values SVR: ', F2020ML.F2020_SVR(dfX, dfY, 0.3, 4))
print('Values RFR: ', F2020ML.F2020_RFR(dfX, dfY, 0.3, 4))
# print(F2020ML.plot_data(dfX, dfY))
