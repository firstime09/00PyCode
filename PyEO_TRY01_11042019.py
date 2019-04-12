import sys
sys.path.append(r"/opt/pyeo")
sen2cor_path = r"/opt/Sen2Cor-02.05.05-Linux64/bin/L2A_Process"
# import pyeo.core as pyeo
from pyeo.pyeo import core as pyeo
import matplotlib.pyplot as plt
import gdal
import pprint
import os

pyeo.init_log("training_log.log")

def show_satellite_image(image_path):
    img = gdal.Open(image_path)
    array = img.GetVirtualMemArray()
    img_view = array.transpose([1,2,0])
    plt.imshow(img_view)
    array = None
    img = None