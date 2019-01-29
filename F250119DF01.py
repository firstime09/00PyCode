from Modul_ML.F17122018ML import F2020ML
import numpy as np
import pandas as pd

# path = 'C:/Users/user/Dropbox/FORESTS2020/00AllData/Data Excel'
path = 'C:/Users/user/Dropbox/FORESTS2020/00AllData'
dframe = pd.read_excel(path + '/Data 580.xlsx')
column = ['Band_4']
target = 'frci'

dfx = pd.DataFrame(dframe, columns=column)
dfy = np.asarray(dframe[target])

print(np.std(dfx))
print(np.mean(dfx))
# print(dframe.groupby(column).apply(np.std))
# print(F2020ML.plot_data(dfx,dfy))
