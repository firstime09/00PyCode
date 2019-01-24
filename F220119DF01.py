import pandas as pd
import numpy as np

def F2020_DF(dframe):
    Load_class = 'Class'
    dclass = np.asarray(dframe[Load_class])
    df1 = pd.Series(dclass).value_counts().reset_index().sort_values('index').reset_index(drop=True)
    df1.columns = ['Class', 'Frequency']
    return df1

path00 = pd.read_excel('D:/00AllData/Data_1048_Yoga.xlsx')
path01 = pd.read_excel('C:/Users/user/Dropbox/FORESTS2020/00AllData/Data From Mas Sahid/FRCI 870_2611N.xlsx')
print(F2020_DF(path00))

## Random new dataframe
# df = pd.DataFrame(np.random.randn(50), path00)
# print(df)

# clss = 'Class'
# dclass = np.asarray(dframe[clss])
# # print(dframe)
# # print(type(dframe.Class[0]))
# df1 = pd.Series(dclass).value_counts().reset_index().sort_values('index').reset_index(drop=True)
# df1.columns = ['Class', 'Frequency']
