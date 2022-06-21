import cv2
import sys
import numpy as np


if __name__ == '__main__':
    img = cv2.imread('lena.jpeg')
    noobcv = cv2.imread('noobcv.jpg')
    if img is None or noobcv is None:
        print('Failed to read img or nooncv.jpg')
        sys.exit()
    mask = cv2.resize(noobcv, (200, 200))
    # 深拷贝
    img1 = img.copy()
    # 浅拷贝
    img2 = img
    # 截取图像ROI区域
    ROI = img[206: 406, 206: 406]
    # 深拷贝
    ROI_copy = ROI.copy()
    # 浅拷贝
    ROI1 = ROI
    img[206: 406, 206:406] = mask

    cv2.imshow('img + noobcv', img1)
    cv2.imshow('img + noobcv2', img2)
    cv2.imshow('ROI copy1', ROI_copy)
    cv2.imshow('ROI_copy2', ROI)

    # 在图像中绘制圆形
    img = cv2.circle(img, (300, 300), 20, (0, 0, 255), -1)

    cv2.imshow('img + circle1', img1)
    cv2.imshow('img + circle2', img2)
    cv2.imshow('ROI circle1', ROI_copy)
    cv2.imshow('ROI', ROI)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

