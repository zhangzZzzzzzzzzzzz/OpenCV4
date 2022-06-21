import cv2
import numpy as np
import sys
# from matplotlib import pyplot as plt
#
#
# #a =np.int32([[1, 2, 6, 4, 3]]).reshape(5,-1)
# #a = ([1], [3], [6])
# a = [[1, 3], [2, 5], [6, 8]]
# print(a)
# plt.plot(a, color='b')
# plt.show()

a = np.random.randint(0, 255, 3)
print(a)
# a = a.ravel()
# print(a)
# print(a.shape)

a = list(map(lambda x: int(x), a))
print(a)