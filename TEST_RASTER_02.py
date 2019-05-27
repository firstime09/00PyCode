from __future__ import print_function, division
from osgeo import gdal, gdal_array
from sklearn.preprocessing import MinMaxScaler
from sklearn.svm import SVR
import matplotlib.pyplot as plt
import openpyxl, numpy as np
import glob, pandas as pd
from Modul_ML.F17122018ML import F2020ML
from sklearn.model_selection import train_test_split
from Modul_Topo.F2020_RASTER import Raster_Func

class Modul_RUN_1:

    def SVR_Model(dataX, dataY, test_size, r_state):
        X_train, X_test, y_train, y_test = train_test_split(dataX, dataY, test_size=test_size, random_state=r_state)
        # sc = MinMaxScaler()
        # X_train = sc.fit_transform(X_train)
        # X_test = sc.transform(X_test)

        best_score = 0
        for C in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
            for gamma in [0.01, 0.1, 0.2, 0.3, 0.4, 0.5, 1]:
                for epsilon in [0.001, 0.01, 0.1, 0.2, 0.3, 0.4, 0.5]:
                    calfSVR = SVR(kernel='rbf', C=C, gamma=gamma, epsilon=epsilon)
                    calfSVR.fit(X_train, y_train)
                    score = calfSVR.score(X_test, y_test)
                    if score > best_score:
                        best_score = score
                        best_C = C
                        best_gam = gamma
                        best_eps = epsilon
                        # best_parm = {'C': best_C, 'Gamma': best_gam, 'Epsilon': best_eps}

        calfSVR_Model = SVR(kernel='rbf', C=best_C, epsilon=best_eps, gamma=best_gam)
        calfSVR_Model.fit(X_train, y_train)
        # calfSVR_Score = calfSVR_Model.score(X_test, y_test)
        # y_pred = calfSVR_Model.predict(X_test)
        # RMSE_Model = F2020ML.F2020_RMSE(y_test, y_pred)
        # R2_Model = F2020ML.F2020_RSQRT(y_test, y_pred)
        # Model = {'RMSE': RMSE_Model, 'R^2': R2_Model}
        return(calfSVR_Model)

    def Stack_raster(self, input_path, name):
        path = input_path
        file_loaction = glob.glob(path + "/*.tif")
        file_virtual = path + "/Stacked_Data.vrt"
        file_tif = path + (name + ".tif")
        virtual = gdal.BuildVRT(file_virtual, file_loaction, separate=True)
        stack_layer = gdal.Translate(file_tif, virtual)
        return stack_layer

    def Save_Raster(out_path1, pred_model, name, ras):
        saved_data = (name + "_Data_FRCI.TIF")
        output_path = (out_path1 + saved_data)
        # raster = ras
        in_path = gdal.Open(ras)
        in_array = pred_model
        proj = in_path.GetProjection()
        geotrans = in_path.GetGeoTransform()
        row = in_path.RasterYSize
        col = in_path.RasterXSize
        driver = gdal.GetDriverByName("GTiff")
        outdata = driver.Create(output_path, col, row, 1, gdal.GDT_Float32)
        outband = outdata.GetRasterBand(1)
        outband.SetNoDataValue(-9999)
        outband.WriteArray(in_array)
        outdata.SetGeoTransform(geotrans)  # Georeference the image
        outdata.SetProjection(proj)  # Write projection information
        outdata.FlushCache()
        outdata = None
        return outdata