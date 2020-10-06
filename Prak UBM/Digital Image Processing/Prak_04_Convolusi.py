import cv2
import numpy as np

location_path = r"D:\00PyCode\Prak UBM\00_Image"
im = cv2.imread(location_path + '/citrababon_png.png')
# b,g,r = cv2.split(im)
# bg = b - g
# blur = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
blur_1 = np.array([[0.04, 0.04, 0.04, 0.04, 0.04], [0.04, 0.04, 0.04, 0.04, 0.04], [0.04, 0.04, 0.04, 0.04, 0.04],
                   [0.04, 0.04, 0.04, 0.04, 0.04], [0.04, 0.04, 0.04, 0.04, 0.04]])
blur_2 = np.array([[0.11, 0.11, 0.11], [0.11, 0.11, 0.11], [0.11, 0.11, 0.11]])
blur_kov_0_1 = np.array([[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]])
blur_kov_0_2 = np.array([[0, -1, 0], [-1, 4, -1], [0, -1, 0]])
blur_kov_1 = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
# filter_1 = cv2.filter2D(im, -1, blur)
# filter_2 = cv2.filter2D(im, -1, blur_2)
filter_3 = cv2.filter2D(im, -1, blur_kov_0_1)
filter_4 = cv2.filter2D(im, -1, blur_kov_0_2)
# bg_filter = cv2.filter2D(bg, -1, blur_kov_1)
#
cv2.imshow('Gambar_RGB', im)
# cv2.imshow('Gambar_BG', bg)
# cv2.imshow('Gambar_Filter_BG', bg)
cv2.imshow('Gambar_filter_1', filter_4)
# cv2.imshow('Gambar_filter_0', filter_3)
# cv2.imshow('Gambar_filter2', filter_2)

cv2.waitKey(0)
cv2.destroyAllWindows()

"""
b,g,r = cv2.split(im)
gr = g-r
blur = cv2.blur(im,(5,5),0)
Gaussblur = cv2.GaussianBlur(im,(7,7),0)
karnel00 = np.array([[1,1,1],[1,1,1],[1,1,1]]) #--- Karnel00 Untuk Lowpass Filter
karnel001 = karnel00*1/16
test0 = cv2.filter2D(gr, -1, karnel001)
karnel01 = np.array([[1,-2,1],[-2,4,-2],[1,-2,1]])
#--- Karnel01 Untuk Highpass Filter karnel01 semua bil.bulat dgn hasil penjumlahan=1
test1 = cv2.filter2D(gr, -1, karnel01)

# print(karnel00)
cv2.imshow("image", im)
# cv2.imshow("blur",blur)
# cv2.imshow("Gauss",Gaussblur)
cv2.imshow("Coba1",test0)
cv2.imshow("Coba2",test1)
# cv2.imshow("Gauss",Gaussblur)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""