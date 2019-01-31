# Boruta algorithm test 01
import pandas as pd
import numpy as np
from boruta import BorutaPy
from sklearn.ensemble import RandomForestRegressor

path = 'C:/Users/user/Dropbox/FORESTS2020/00AllData/'
dfxlx = pd.read_excel(path + '30001_Cidanau_580_NEW.xlsx')
# print(dframe)
column = ['Band_2', 'Band_3', 'Band_4', 'Band_5', 'Band_6', 'Band_7']
# column = ['Band_2', 'Band_4', 'Band_6']
# column = ['Band_3', 'Band_5', 'Band_7']
target = 'frci'
dfX = pd.DataFrame(dfxlx, columns=column)
dfY = np.asarray(dfxlx[target])

clfRFR = RandomForestRegressor(n_jobs=-1, max_depth=5)
feat_selector = BorutaPy(clfRFR, n_estimators='auto', verbose=2, random_state=1)

hasil = feat_selector.fit(dfX, dfY)
print(hasil)
