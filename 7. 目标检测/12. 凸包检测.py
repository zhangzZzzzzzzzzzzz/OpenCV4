import cv2
import numpy as np


if __name__ == '__main__':
    image = cv2.imread('hand.png')
    # 灰度化
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # 二值化
    _, binary = cv2.threshold(gray, 105, 255, cv2.THRESH_BINARY)
    cv2.imshow('erzhi', binary)
    # 对图像进行开运算
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (9, 9), (-1, -1))
    binary = cv2.morphologyEx(binary, cv2.MORPH_OPEN, kernel)
    cv2.imshow('Open', binary)
    # 轮廓检测
    contours, hierarchy = cv2.findContours(binary, mode=cv2.RETR_TREE, method=cv2.CHAIN_APPROX_SIMPLE)
    # 计算并绘制凸包
    for i in contours:
        hull = cv2.convexHull(i)
        # 绘制边缘
        image = cv2.drawContours(image, [hull], -1, (0, 0, 255), 2, 8)
        # 绘制顶点
        for j in hull:
            cv2.circle(image, (j[0, 0], j[0][1]), 4, (255, 0, 0), 2, 8, 0)
    cv2.imshow('Convexhull', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()