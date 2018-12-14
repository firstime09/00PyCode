import pandas as pd
import numpy as np
import math, My_Function
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVR
from sklearn.model_selection import train_test_split

SVR_Model = My_Function.allFunction
def rSquared(ActualY, EstimatedY):
	rScore = (1 - sum((ActualY-EstimatedY)**2) / sum((ActualY-ActualY.mean(axis=0))**2))
	return float(rScore)

def rMSE(ActualY, EstimatedY):
	rootMSE = (math.sqrt(sum((ActualY-EstimatedY)**2) / ActualY.shape[0]))
	return rootMSE

df = pd.read_excel('C:/Users/user/Dropbox/FORESTS2020/00AllData/Data 580.xlsx')
# print(df.head())
features = df.columns.drop(['FID','Shape *','frci','Class','Band_1'])
targets = 'frci'
dataX = np.asarray(df[features])
dataY = np.asarray(df[targets])

# Best Model SVR """(0.609670937612555, {'C': 1, 'gamma': 1, 'epsilon': 0.1})"""
X_train, X_test, y_train, y_test = train_test_split(dataX, dataY, train_size=0.3, random_state=4)
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

clfSVR = SVR(kernel='rbf', C=1, epsilon=0.1, gamma=1)
clfSVR.fit(X_train, y_train)
scores = clfSVR.score(X_test, y_test)
y_pred = clfSVR.predict(X_test)
print(scores)
print('R Squared: ', rSquared(y_test, y_pred), '+++++', 'RMSE: ', rMSE(y_test, y_pred))
