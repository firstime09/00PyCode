# import pandas as pd
# from matplotlib import pyplot as plt

from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
from matplotlib import cm

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
X = [1, 2, 3, 4, 5, 6, 7, 8]
Y = [3, 2, 5, 1, 7, 9, 7, 10]
Z = [0, 3, 5, 1, 4, 5, 8, 10]
ax.scatter(X, Y, Z, c='r', marker='o')
ax.set_xlabel('x axis')
ax.set_ylabel('y axis')
ax.set_zlabel('z axis')

plt.show()
# X, Y, Z = axes3d.get_test_data(0.05)
# ax.plot_surface(X, Y, Z, rstride=8, cstride=8, alpha=0.3)
# cset = ax.contour(X, Y, Z, zdir='z', offset=-100, cmap=cm.coolwarm)
# cset = ax.contour(X, Y, Z, zdir='x', offset=-40, cmap=cm.coolwarm)
# cset = ax.contour(X, Y, Z, zdir='y', offset=40, cmap=cm.coolwarm)
#
# ax.set_xlabel('X')
# ax.set_xlim(-40, 40)
# ax.set_ylabel('Y')
# ax.set_ylim(-40, 40)
# ax.set_zlabel('Z')
# ax.set_zlim(-100, 100)
#
# plt.show()

# def plot_data(DataX, DataY, DataZ):
#     plt.plot(DataX, DataY)
#     plt.plot(DataX, DataZ)
#     plt.title('Test Plot Data')
#     plt.xlabel('X')
#     plt.ylabel('Y and Z')
#     plt.legend(['Line of Y','Line of Z'])
#     plt.show()
#
#
# # if i have the vector Data
# X = [1, 3, 6]
# Y = [2, 5, 8]
# Z = [7, 4, 9]
#
# print(plot_data(X, Y, Z))
