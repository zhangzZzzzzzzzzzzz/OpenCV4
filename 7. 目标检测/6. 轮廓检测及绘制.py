import cv2
import sys


if __name__ == '__main__':
    image = cv2.imread('circles.png')
    cv2.imshow('Origin', image)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # 高斯滤波
    gray = cv2.GaussianBlur(gray, (9, 9), sigmaX=2, sigmaY=2)
    cv2.imshow('gray', gray)
    # 二值化
    _, binary = cv2.threshold(gray, 75, 180, cv2.THRESH_BINARY)
    cv2.imshow('binary', binary)
    # 轮廓检测
    contours, hierarchy = cv2.findContours(binary, mode=cv2.RETR_TREE, method=cv2.CHAIN_APPROX_SIMPLE)
    # 轮廓绘制
    image = cv2.drawContours(image, contours, -1, (0, 0, 255), 2, cv2.LINE_8)
    # 输出轮廓层级关系
    print(hierarchy)

    cv2.imshow('Find and Draw Contours', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
