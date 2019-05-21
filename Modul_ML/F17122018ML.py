import math, numpy, pandas, os, glob
from osgeo import gdal
from matplotlib import pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVR
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

class F2020ML:
    def plot_data(DataX, DataY): #--- Data Visualization 2D 16/01-2019
        plt.plot(DataX, DataY)
        plt.scatter(DataX, DataY, label="Data", marker="*", s=30)
        plt.title('Data Visualization')
        plt.xlabel('Data X')
        plt.ylabel('Data Y')
        plt.legend()
        plt.show()

    def export_array(in_path, in_array, output_path): #--- For map of array from Mr. Sahid (13/12-2018)
        """This function is used to produce output of array as a map."""
        global proj, geotrans, row, col
        proj        = in_path.GetProjection()
        geotrans    = in_path.GetGeoTransform()
        row         = in_path.RasterYSize
        col         = in_path.RasterXSize
        driver      = gdal.GetDriverByName("GTiff")
        outdata     = driver.Create(output_path, col, row, 1, gdal.GDT_CFloat32)
        outband     = outdata.GetRasterBand(1)
        outband.SetNoDataValue(-9999)
        outband.WriteArray(in_array)
        outdata.SetGeoTransform(geotrans) # Georeference the image
        outdata.SetProjection(proj) # Write projection information
        outdata.FlushCache()
        outdata = None
        return outdata

    def readRaster(path, dem):
        # Read Data Landsat 8 and Sentinel 2
        raster_list = glob.glob(path + '*.TIF')
        read = []
        for i in raster_list:
            band = gdal.Open(i)
            read.append(band.GetRasterBand(1).ReadAsArray().astype(float))
        filename = []
        for a in [os.path.basename(x) for x in glob.glob(path + '*.TIF')]:
            p = os.path.splitext(a)[0]
            filename.append(p)
        my_dict = dict(zip(filename, read))
        # Read Data Sentinel DEM
        raster_list_dem = glob.glob(dem + '*.TIF')
        read_dem = []
        for j in raster_list_dem:
            band_dem = gdal.Open(j)
            read_dem.append(band_dem.GetRasterBand(1).ReadAsArray().astype(float))
        return (my_dict, read_dem)

    def F2020_DF(dframe):
        Load_class = 'Class'
        dclass = numpy.asarray(dframe[Load_class])
        df1 = pandas.Series(dclass).value_counts().reset_index().sort_values('index').reset_index(drop=True)
        df1.columns = ['Class', 'Frequency']
        a = df1.min()
        return a

    def F2020_RSQRT(ActualY, PredictY): #--- value of r^2 in statistic (04/12-2018)
        rScores = (1 - sum((ActualY - PredictY)**2) / sum((ActualY - ActualY.mean(axis=0))**2))
        return rScores

    def F2020_RMSE(ActualY, PredictY): #--- Root mean squared error in statistical model (04/12-2018)
        rootMSE = (math.sqrt(sum((ActualY-PredictY)**2) / ActualY.shape[0]))
        return rootMSE

    def F2020_MinMax(data): #--- Min Max Normalization model (18/03-2-19)
        Norm_MinMax = (data - numpy.min(data)) / (numpy.max(data) - numpy.min(data))
        return Norm_MinMax

    def F2020_ZScore(data): #--- ZScore Normalization model (18/03-2-19)
        Norm_ZScore = (data - numpy.mean(data)) / (numpy.std(data))
        return Norm_ZScore

    def F2020_SVR(dataX, dataY, tsize, rstate): #--- Model SVR kernel radial basis function FORESTS2020
        X_train, X_test, y_train, y_test = train_test_split(dataX, dataY, test_size=tsize, random_state=rstate)
        sc = StandardScaler()
        # sc.fit(X_train)
        X_train = sc.fit_transform(X_train)
        X_test = sc.transform(X_test)
        best_score = 0
        for C in [0.001, 0.01, 0.1, 1, 10, 100]:
            for gamma in [0.001, 0.01, 0.1, 1, 10, 100]:
                for epsilon in [0.001, 0.01, 0.1, 1, 10, 100]:
                    # Train Model SVR
                    clfSVR = SVR(kernel='rbf', C=C, gamma=gamma, epsilon=epsilon)
                    clfSVR.fit(X_train, y_train)
                    score = clfSVR.score(X_test, y_test)
                    if score > best_score:
                        best_score = score
                        best_parameters = {'C': C, 'gamma': gamma, 'epsilon': epsilon}
        return(best_score, best_parameters)

    def F2020_RFR(dataX, dataY, tsize, rstate): #--- Random Forest Regressor Model
        X_train, X_test, y_train, y_test = train_test_split(dataX, dataY, test_size=tsize, random_state=rstate)
        sc = StandardScaler()
        X_train = sc.fit_transform(X_train)
        X_test = sc.transform(X_test)
        best_score = 0
        for n_esti in [10, 20, 30, 40, 50, 100]:
            # Train Model Random Forest
            clfRFR = RandomForestRegressor(n_estimators=n_esti, random_state=rstate)
            clfRFR.fit(X_train, y_train)
            score = clfRFR.score(X_test, y_test)
            if score > best_score:
                best_score = score
                total_tree = {'n_estimators': n_esti}
        return(best_score, total_tree)
