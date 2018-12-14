import pandas as pd
import numpy as np
import math, My_Function
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

SVR_Model = My_Function.allFunction
def rSquared(ActualY, EstimatedY):
	rScore = (1 - sum((ActualY-EstimatedY)**2) / sum((ActualY-ActualY.mean(axis=0))**2))
	return float(rScore)

def rMSE(ActualY, EstimatedY):
	rootMSE = (math.sqrt(sum((ActualY-EstimatedY)**2) / ActualY.shape[0]))
	return rootMSE

df = pd.read_excel('C:/Users/user/Dropbox/FORESTS2020/00AllData/Data 580.xlsx')
features = df.columns.drop(['FID','Shape *','frci','Class','Band_1'])
targets = 'frci'
dataX = np.asarray(df[features])
dataY = np.asarray(df[targets])

X_train, X_test, y_train, y_test = train_test_split(dataX, dataY, test_size=0.3, random_state=4)
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

clfRFR = RandomForestRegressor(n_estimators=30, random_state=4)
clfRFR.fit(X_train, y_train)
y_pred = clfRFR.predict(X_test)
RSquare = rSquared(y_test, y_pred)
print('RSquared: ', RSquare, '+++++', 'RMSE: ', rMSE(y_test, y_pred))
