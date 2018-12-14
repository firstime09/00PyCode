import numpy as np
import math, pandas as pd
import matplotlib.pyplot as plt
# from My_Function import allFunction
from sklearn.metrics import r2_score, mean_squared_error
from sklearn.cross_decomposition import PLSRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# RSquare = allFunction.rSquared
# RMSE = allFunction.rMSE

df = pd.read_excel('C:/Users/user/Dropbox/MyDocument/Data Nitrogen - Lexi Pendong.xlsx')
# print(df.head(), '\n', df.describe()) ## For summary data
features = df.columns.drop(['Jenis','Nitrogen'])
targets = 'Nitrogen'
dfX = np.asarray(df[features])
dfY = np.asarray(df[targets])

X_train, X_test, y_train, y_test = train_test_split(dfX, dfY, test_size=0.3, random_state=0)
# sc = StandardScaler()
# X_train = sc.fit_transform(X_train)
# X_test = sc.transform(X_test)

clfPLS = PLSRegression(n_components=2, scale=True)
clfPLS.fit(X_train, y_train)
y_pred = clfPLS.predict(X_test)
## Make Plot data
# plt.subplot(221)
# plt.plot(X_train, y_train, 'ro', linewidth=2.0)
# plt.plot(X_test, y_test, 'ro', linewidth=2.0)
plt.plot(y_test, y_pred, 'ro')
plt.yscale('linear')
plt.xlabel("Data X")
plt.ylabel("Data Y")
# plt.legend()
plt.show()

# print('Accuracy PLS: ', clfPLS.score(X_test, y_test))
# print('RSquared: ', RSquare(y_test, y_pred))
# print('RMSE: ', math.sqrt(mean_squared_error(y_test, y_pred)))
