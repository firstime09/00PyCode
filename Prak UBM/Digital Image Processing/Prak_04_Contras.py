import cv2

location_path = r"D:\00PyCode\Prak UBM\00_Image"
image = cv2.imread(location_path + '/citrababon_png.png')
# image = cv2.imread('1.jpg')

alpha = 2 # Contrast control (1.0-3.0)
beta = 50 # Brightness control (0-100)

adjusted = cv2.convertScaleAbs(image, alpha=alpha, beta=beta)

cv2.imshow('original', image)
cv2.imshow('adjusted', adjusted)
cv2.waitKey()