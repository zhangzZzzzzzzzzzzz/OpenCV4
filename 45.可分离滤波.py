import cv2
import numpy as np
import sys


if __name__ == '__main__':
    # 验证滤波算法的数据矩阵
    data = np.array([[1, 2, 3, 4, 5],
                     [6, 7, 8, 9, 10],
                     [11, 12, 13, 14, 15],
                     [16, 17, 18, 19, 20],
                     [21, 22, 23, 24, 25]], np.float32)

    # 构建滤波器
    a = np.array([[-1], [3], [-1]])
    b = a.reshape((1, 3))
    ab = a * b

    # 验证高斯滤波器的可分离性
    # 构建高斯滤波器
    gaussX = cv2.getGaussianKernel(3, 1)
    gauss_data = cv2.GaussianBlur(data, (3, 3), 1, None, 1, cv2.BORDER_CONSTANT)
    gauss_data_XY = cv2.sepFilter2D(data, -1, gaussX, gaussX, None, (-1, -1), 0, cv2.BORDER_CONSTANT)
    print('采用cv2.GaussianBlur:\n{}'.format(gauss_data))
    print('采用cv2.sepFilter2D:\n{}'.format(gauss_data_XY))

    # 验证线性滤波的可分离性
    data_Y = cv2.filter2D(data, -1, a, None, (-1, -1), 0, cv2.BORDER_CONSTANT)
    data_YX = cv2.filter2D(data_Y, -1, b, None, (-1, -1), 0, cv2.BORDER_CONSTANT)
    data_XY = cv2.filter2D(data, -1, ab, None, (-1, -1), 0, cv2.BORDER_CONSTANT)
    data_XX_sep = cv2.sepFilter2D(data, -1, b, b, None, (-1, -1), 0, cv2.BORDER_CONSTANT)
    data_XY_sep = cv2.sepFilter2D(data, -1, a, b, None, (-1, -1), 0, cv2.BORDER_CONSTANT)
    print('data_Y=\n{}'.format(data_Y))
    print('data_YX=\n{}'.format(data_YX))
    print('data_XY=\n{}'.format(data_XY))
    print('data_XX_sep=\n{}'.format(data_XX_sep))
    print('data_XY_sep=\n{}'.format(data_XY_sep))

    # 对图像进行分离操作
    img = cv2.imread('lena.jpeg')
    if img is None:
        print('Failed to read img')
        sys.exit()
    img_Y = cv2.filter2D(img, -1, a, None, (-1, -1), 0, cv2.BORDER_CONSTANT)
    img_YX = cv2.filter2D(img_Y, -1, b, None, (-1, -1), 0, cv2.BORDER_CONSTANT)
    img_XY = cv2.filter2D(img, -1, ab, None, (-1, -1), 0, cv2.BORDER_CONSTANT)
    cv2.imshow('img_Y', img_Y)
    cv2.imshow('img_YX', img_YX)
    cv2.imshow('img_XY', img_XY)
    cv2.waitKey(0)
    cv2.destroyAllWindows()



