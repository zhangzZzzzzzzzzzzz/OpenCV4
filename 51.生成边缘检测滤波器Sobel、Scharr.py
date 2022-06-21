import cv2
import numpy as np
import sys


if __name__ == '__main__':
    # 一阶x方向的Sobel算子 3*3的
    sobel_x1, sobel_y1 = cv2.getDerivKernels(1, 0, 3)
    sobel_X1 = sobel_y1 * sobel_x1.T
    print('一阶x方向的Sobel算子：\n{}'.format(sobel_X1))
    # 二阶x方向的Sobel算子 5*5的
    sobel_x2, sobel_y2 = cv2.getDerivKernels(2, 0, 5)
    sobel_X2 = sobel_y2 * sobel_x2.T
    print('二阶x方向的Sobel算子：\n{}'.format(sobel_X2))
    # 三阶x方向的Sobel算子 7*7
    sobel_x3, sobel_y3 = cv2.getDerivKernels(3, 0, 7)
    sobel_X3 = sobel_y3 * sobel_x3.T
    print('三阶x方向的Sobel算子：\n{}'.format(sobel_X3))

    # 一阶x方向的Scharr算子
    scharr_x1, scharr_y1= cv2.getDerivKernels(1, 0, cv2.FILTER_SCHARR)
    scharr_X1 = scharr_y1 * scharr_x1.T
    print('一阶x方向的Scharr算子：\n{}'.format(scharr_X1))


