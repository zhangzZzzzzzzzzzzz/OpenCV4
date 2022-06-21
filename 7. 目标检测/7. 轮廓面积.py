import cv2
import sys
import numpy as np


if __name__ == '__main__':
    # 用4个点表示三角形轮廓
    A = (0, 0)
    B = (10, 0)
    C = (10, 10)
    D = (5, 5)
    triangle = np.array((A, B, C, D))
    triangle_area = cv2.contourArea(triangle)
    print('三角形面积为：{}'.format(triangle_area))

    image = cv2.imread('circles.png')
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # 高斯滤波
    gray = cv2.GaussianBlur(gray, (9, 9), sigmaX=2, sigmaY=2)
    # 二值化
    binary = cv2.threshold(gray, 75, 180, cv2.THRESH_BINARY)
    # 轮廓检测
    contours, hierarchy = cv2.findContours(binary[1], mode=cv2.RETR_TREE, method=cv2.CHAIN_APPROX_SIMPLE)
    # 输出各个轮廓面积
    for i in range(len(contours)):
        img_area = cv2.contourArea(contours[i])
        print('第{}个轮廓面积：{}'.format(i, img_area))
