import numpy as np
import cv2, glob

def split_image(img):
    (r, g, b) = cv2.split(img)
    img_split = [np.mean(r), np.mean(g), np.mean(b),
                np.std(r), np.std(g), np.std(b)]
    return img_split

path = 'D:/00PyCode/00AllData/Data Image/forest/*.jpg'
for data in glob.glob(path):
    load_data = cv2.imread(data)
    proses = split_image(load_data)
    print(proses)
