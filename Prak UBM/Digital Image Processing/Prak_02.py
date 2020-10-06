import numpy as np

Matriks_R = np.array([[1, 2, 3], [1, 1, 1], [3, 2, 1]])
Matriks_G = np.array([[1, 0, 1], [2, 1, 3], [1, 2, 1]])
Matriks_B = np.array([[2, 3, 3], [2, 2, 0], [3, 1, 0]])

Matriks_RGB = Matriks_R + Matriks_G + Matriks_B
Matriks_Gray = Matriks_RGB / 3
print(Matriks_RGB)
print(Matriks_Gray)

# value_of_MatriksRGB =