import cv2
import sys
import numpy as np


if __name__ == '__main__':
    img = cv2.imread('equalLena.png', cv2.IMREAD_ANYDEPTH)
    # 验证方框滤波算法的矩阵
    points = np.array([[1, 2, 3, 4, 5],
                       [6, 7, 8, 9, 10],
                       [11, 12, 13, 14, 15],
                       [16, 17, 18, 19, 20],
                       [21, 22, 23, 24, 25]], np.float32)
    # 将图像转化为float32 类型的数据
    img_32 = img.astype('float32')
    img_32 = img_32/255.0

    # 方框滤波
    # 进行归一化, 进行归一化时 cv2.boxFilter与cv2.blur输出相同
    img_box_norm = cv2.boxFilter(img_32, -1, (3, 3), normalize=True)
    img_mean = cv2.blur(img_32, (3, 3))

    # 不进行归一化
    img_box = cv2.boxFilter(img_32, -1, (3, 3), normalize=False)

    # 平方方框滤波
    # 进行归一化
    img_sqr_norm = cv2.sqrBoxFilter(img_32, -1, (3, 3), normalize=True, borderType=cv2.BORDER_CONSTANT)
    points_sqr_norm = cv2.sqrBoxFilter(points, -1, (3, 3), normalize=True, borderType=cv2.BORDER_CONSTANT)
    # 不进行归一化
    points_srq = cv2.sqrBoxFilter(points, -1, (3, 3), normalize=False, borderType=cv2.BORDER_CONSTANT)
    print(points_sqr_norm)
    print(points_srq)
    cv2.imshow('img_box_norm', img_box_norm)
    cv2.imshow('img_box_mean', img_mean)
    cv2.imshow('img_box', img_box)
    cv2.imshow('img_sqr_norm1', img_sqr_norm)
    cv2.imshow('img_sqr_norm2', img_sqr_norm / np.max(img_sqr_norm))
    cv2.waitKey(0)
    cv2.destroyAllWindows()
