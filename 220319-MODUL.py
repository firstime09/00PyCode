import numpy as np
from sklearn.svm import SVR
from sklearn.preprocessing import MinMaxScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

class SVR_Vs_RFR:

    def SVR_Modul(dataX, dataY, tsize, rstate):
        X_train, X_test, y_train, y_test = train_test_split(dataX, dataY, test_size=tsize, random_state=rstate)
        sc = MinMaxScaler()
        X_train = sc.fit_transform(X_train)
        X_test = sc.transform(X_test)
        best_score = 0
        for C in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
            for gamma in [0.001, 0.01, 0.1, 0.2, 1, 2]:
                for epsilon in [0.0001, 0.001, 0.01, 0.1, 1, 5]:
                    clfSVR = SVR(kernel='rbf', C=C, gamma=gamma, epsilon=epsilon)
                    clfSVR.fit(X_train, y_train)
                    score = clfSVR.score(X_test, y_test)
                    if score > best_score:
                        best_score = score
                        best_parm = {'C':C, 'Gamma':gamma, 'Epsilon':epsilon}
        return(best_score, best_parm)

    def RFR_Modul(dataX, dataY, tsize, rsate):
        X_train, X_test, y_train, y_test = train_test_split(dataX, dataY, test_size=tsize, random_state=rsate)
        sc = MinMaxScaler()
        X_train = sc.fit_transform(X_train)
        X_test = sc.transform(X_test)
        best_score = 0
        for n_esti in [5, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]:
            clfRFR = RandomForestRegressor(n_estimators=n_esti, random_state=rsate)
            clfRFR.fit(X_train, y_train)
            score = clfRFR.score(X_test, y_test)
            if score > best_score:
                best_score = score
                best_parm = {'n_estimators':n_esti}
        return(best_score, best_parm)