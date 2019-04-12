## Optimization parameters using Grid-Search Algorithm 
import pandas as pd
import numpy as np
from sklearn.metrics import classification_report
from sklearn.svm import SVR
from sklearn.model_selection import GridSearchCV, train_test_split

path = 'D:/00RCode/Result/01042019_JOIN_DF_LINE_1.2/'
loadDF = pd.read_excel(path + 'CIDANAU_LINE_1_2_SUMATERA_77_14.xlsx')
select_col = ['Band_2', 'Band_3', 'Band_4', 'Band_5', 'Band_6', 'Band_7']
select_row = 'frci'
dfx = pd.DataFrame(loadDF, columns=select_col)
dfy = np.asarray(loadDF[select_row])

X_train, X_test, y_train, y_test = train_test_split(dfx, dfy, test_size=0.3, random_state=5)
params = {'kernel': ['rbf'], 'C': [1, 10], 'Gamma': [0.01, 1], 'Epsilon': [0.001, 0.01]}
clfSVR = SVR()
grid = GridSearchCV(clfSVR, params)
grid_result = grid.fit(X_train, y_train)