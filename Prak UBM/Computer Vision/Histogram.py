import cv2
import matplotlib.pyplot as plt

location_path = r"D:\00PyCode\Prak UBM\00_Image"
img_1 = cv2.imread(location_path + '/citrababon_bmp.bmp')
b, g, r = cv2.split(img_1)
histogram = cv2.calcHist([img_1], [0], None, [256], [0, 256])

cv2.imshow('Name_RGB', img_1)
cv2.imshow('Name_b', b)
cv2.imshow('Name_g', g)
cv2.imshow('Name_r', r)
plt.plot(histogram)
plt.show()

#Opsional
"""cv2.imshow('Name',img_1)
cv2.waitKey(0)
cv2.destroyAllWindows()"""