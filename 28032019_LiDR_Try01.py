from laspy.file import File
import numpy as np

path = 'D:/00AllData/Data LiDAR/07. POINT CLOUD/'
load_data = File(path + 'AREA_1_ALL _CLASS.las', mode='r')
print(load_data)