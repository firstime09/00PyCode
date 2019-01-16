import pandas as pd
from matplotlib import pyplot as plt

def plot_data(DataX, DataY, DataZ):
    plt.plot(DataX, DataY)
    plt.plot(DataX, DataZ)
    plt.title('Test Plot Data')
    plt.xlabel('X')
    plt.ylabel('Y and Z')
    plt.legend(['Line of Y','Line of Z'])
    plt.show()


# if i have the vector Data
X = [1, 3, 6]
Y = [2, 5, 8]
Z = [7, 4, 9]

print(plot_data(X, Y, Z))
