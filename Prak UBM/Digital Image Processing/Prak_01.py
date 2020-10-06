'''Cara Membuat matriks'''
import cv2
import numpy as np

Matriks_A = np.array(([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 2, 1, 0, 0, 0, 0, 0, 0, 0],
                       [0, 1, 3, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
                       [0, 0, 2, 2, 0, 4, 3, 0, 0, 0],
                       [0, 0, 4, 3, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 1, 3, 3, 5, 10],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]), dtype=np.uint8)

Matriks_B = np.array(([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 2, 1, 0, 0, 0, 0, 0, 0, 0],
                       [0, 1, 3, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
                       [0, 0, 2, 2, 0, 4, 3, 0, 0, 0],
                       [0, 0, 4, 3, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 10, 20, 10, 10, 10, 10],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]), dtype=np.uint8)

Matriks_C = np.array(([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 2, 1, 0, 0, 0, 0, 0, 0, 0],
                       [0, 1, 3, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
                       [0, 0, 2, 2, 0, 4, 3, 0, 0, 0],
                       [0, 0, 4, 3, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 10, 40, 50, 60, 60],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]), dtype=np.uint8)
print(Matriks_A)
new_img = cv2.merge([Matriks_A, Matriks_B, Matriks_C])
dir_save = r"D:\00PyCode\Prak UBM\Digital Image Processing\Hasil"
cv2.imwrite(dir_save + "/Test_Img_10x10_.png", new_img)
cv2.imshow("Test_img_create", new_img)
cv2.waitKey(0)


Matriks_R = np.array([[1, 2, 3], [1, 1, 1], [3, 2, 1]])
Matriks_G = np.array([[1, 0, 1], [2, 1, 3], [1, 2, 1]])
Matriks_B = np.array([[2, 3, 3], [2, 2, 0], [3, 1, 0]])

Mtriks_RGB = Matriks_R + Matriks_G + Matriks_B
Mtriks_gray = ((Matriks_R + Matriks_G + Matriks_B)/3)
print(Mtriks_gray)