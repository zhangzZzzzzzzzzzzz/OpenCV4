import cv2
import sys
import numpy as np


if __name__ == '__main__':
    image = cv2.imread('stuff.jpg')
    cv2.imshow('Origin', image)
    # 提取图像边缘
    canny = cv2.Canny(image, 80, 160, 3)
    cv2.imshow('Canny Image', canny)
    # 膨胀运算
    kernel = cv2.getStructuringElement(0, (3, 3))
    canny = cv2.dilate(canny, kernel=kernel)
    cv2.imshow('dilate', canny)
    # 轮廓检测及绘制
    contours, hierarchy = cv2.findContours(canny, mode=cv2.RETR_EXTERNAL, method=cv2.CHAIN_APPROX_SIMPLE)
    # 寻找外接多边形
    img1 = image.copy()
    img2 = image.copy()
    for i in range(len(contours)):
        # 绘制最大外接矩形
        max_rect = cv2.boundingRect(contours[i])
        cv2.rectangle(img1, max_rect, (0, 0, 255), 2, 8, 0)
        # 绘制最小外接矩形
        min_rect = cv2.minAreaRect(contours[i])
        print(min_rect)
        points = cv2.boxPoints(min_rect).astype(np.int64)
        print(points)
        img2 = cv2.drawContours(img2, [points], -1, (0, 255, 0), 2, 8)

    cv2.imshow('max', img1)
    cv2.imshow('min', img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()