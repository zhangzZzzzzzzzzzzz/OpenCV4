import cv2
import numpy as np
import sys


if __name__ == '__main__':
    # 矩阵垂直、水平连接
    A = np.array([[1, 7], [2, 8]])
    B = np.array([[4, 10], [5, 11]])
    # 垂直连接
    V_C = cv2.vconcat((A, B))
    # 水平连接
    H_C = cv2.hconcat((A, B))
    print('垂直连接结果：\n{}'.format(V_C))
    print('水平连接结果：\n{}'.format(H_C))

    # 图像垂直、水平连接
    img00 = cv2.imread('lena00.jpg')
    img01 = cv2.imread('lena01.jpg')
    img10 = cv2.imread('lena10.jpg')
    img11 = cv2.imread('lena11.jpg')
    # 图像水平连接
    img0 = cv2.hconcat((img00, img01))
    img1 = cv2.hconcat((img10, img11))
    # 图像垂直连接
    img = cv2.vconcat((img0, img1))

    cv2.imshow('img00', img00)
    cv2.imshow('img01', img01)
    cv2.imshow('img10', img10)
    cv2.imshow('img11', img11)
    cv2.imshow('img0', img0)
    cv2.imshow('img1', img1)
    cv2.imshow('img', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
