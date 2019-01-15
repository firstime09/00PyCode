import cv2
import numpy as np

img = cv2.imread("D:/CIKABAYAN/00Test Data/DJI_0171.jpg")
b, g, r = cv2.split(img)
gr = r - g
cv2.imwrite("Result/New_DJI_0171_00.jpg", cv2.Canny(gr, 200, 300))
# cv2.imshow("Result", gr)
cv2.waitKey()
cv2.destroyAllWindows()
