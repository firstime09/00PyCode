import pandas as pd
import numpy as np
from F17122018ML02 import F2020ML

dframe = pd.read_excel('C:/Users/user/Dropbox/FORESTS2020/00AllData/Data From Mas Sahid/FRCI 870_2611NEW.xlsx')
# print(dframe.head())
column = ['Band_2', 'Band_3', 'Band_4', 'Band_5', 'Band_6', 'Band_7']
target = 'FRCI'
dframeX = pd.DataFrame(dframe, columns=column)
dframeY = np.asarray(dframe[target])
# Check SVR and RFR parameters
print('Values SVR: ', F2020ML.F2020_SVR(dframeX, dframeY, 0.3, 4))
print('Values RFR: ', F2020ML.F2020_RFR(dframeX, dframeY, 0.3, 4))
