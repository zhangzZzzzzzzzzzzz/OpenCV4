import cv2
import numpy as np
import sys


if __name__ == '__main__':
    image = cv2.imread('equalLena.png')
    if image is None:
        print('Failed to read img')
        sys.exit()
    # 创建边缘检测滤波器
    kernel1 = np.array([1, -1])
    kernel2 = np.array([1, 0, -1])
    kernel3 = kernel2.reshape((3, 1))
    kernel4 = np.array([1, 0, 0, -1]).reshape((2, 2))
    kernel5 = np.array([0, -1, 1, 0]).reshape((2, 2))

    # 检测图像的边缘
    # 使用[1, -1]检测水平方向边缘
    res1 = cv2.filter2D(image, cv2.CV_16S, kernel1)
    res1 = cv2.convertScaleAbs(res1)
    # 使用[1, 0, -1]检测水平方向边缘
    res2 = cv2.filter2D(image, cv2.CV_16S, kernel2)
    res2 = cv2.convertScaleAbs(res2)
    # 使用[1, 0, -1]检测垂直方向边缘
    res3 = cv2.filter2D(image, cv2.CV_16S, kernel3)
    res3 = cv2.convertScaleAbs(res3)
    # 整幅图像的边缘
    res = res2 + res3
    # 检测Robrts算子45度梯度方向
    res4 = cv2.filter2D(image, cv2.CV_16S, kernel4)
    res4 = cv2.convertScaleAbs(res4)
    res5 = cv2.filter2D(image, cv2.CV_16S, kernel5)
    res5 = cv2.convertScaleAbs(res5)

    cv2.imshow('res1', res1)
    cv2.imshow('res2', res2)
    cv2.imshow('res3', res3)
    cv2.imshow('res', res)
    cv2.imshow('res4', res4)
    cv2.imshow('res5', res5)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
