import cv2
import numpy as np
import sys


if __name__ == '__main__':
    # 矩阵例子
    src = np.array([[1, 2, 3, 4, 5],
                    [6, 7, 8, 9, 10],
                    [11, 12, 13, 14, 15],
                    [16, 17, 18, 19, 20],
                    [21, 22, 23, 24, 25]], np.float32)
    kernel1 = np.array([[1, 1, 1],
                       [1, 1, 1],
                       [1, 1, 1]], np.float32) / 9
    result = cv2.filter2D(src, -1, kernel1)
    print('卷积前的矩阵：\n{}'.format(src))
    print('卷积后的矩阵：\n{}'.format(result))

    # 图像例子
    img = cv2.imread('lena.jpeg')
    kernel2 = np.ones((7, 7), np.float32) / 49
    result2 = cv2.filter2D(img, -1, kernel2)
    cv2.imshow('Origin Image', img)
    cv2.imshow('result2', result2)

    # 模板不对称时， 需旋转180度
    dst = cv2.flip(src, -1)
    print('原卷积模板：\n{}'.format(src))
    print('翻转180度的模板:\n{}'.format(dst))
    cv2.waitKey(0)
    cv2.destroyAllWindows()