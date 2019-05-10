from __future__ import print_function, division
import sys, glob
from osgeo import gdal, gdal_array
from Modul_ML.F17122018ML import F2020ML
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

gdal.UseExceptions()
gdal.AllRegister()

#### stack layer data
path_layer = r"F:\All Data Forests2020\Path112Row56 Manado\TOA MANADO"
file_layer = glob.glob(path_layer + "/TOA MANADOData_Manado_07052019.tiff")
# system('gdal_merge -o cidanau_stack.tif {fileraster}'.format(fileraster=file_layer))
# gm.main(['', '-o', 'cidanau_stack.tif', '{fileraster}'.format(fileraster=file_layer)])
file_vrt = path_layer + "/stacked.vrt"
file_tif = path_layer + "/cidanau_stack.tif"
vrt = gdal.BuildVRT(file_vrt, file_layer, separate=True)
stack_layer = gdal.Translate(file_tif, vrt)