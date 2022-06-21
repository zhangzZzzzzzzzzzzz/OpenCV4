import cv2
import numpy as np
import sys

if __name__ == '__main__':
    img = cv2.imread('lena.jpeg')
    if img is None:
        print('Failed to read img')
        sys.exit()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # 彩色图像二值化
    _, img_B = cv2.threshold(img, 125, 255, cv2.THRESH_BINARY)
    _, img_B_V = cv2.threshold(img, 125, 255, cv2.THRESH_BINARY_INV)
    cv2.imshow('img_B', img_B)
    cv2.imshow('img_B_V', img_B_V)

    # 灰度图像二值化
    _, gray_B = cv2.threshold(gray, 125, 255, cv2.THRESH_BINARY)
    _, gray_B_V = cv2.threshold(gray, 125, 255, cv2.THRESH_BINARY_INV)
    cv2.imshow('gray_B', gray_B)
    cv2.imshow('gray_B_V', gray_B_V)

    # 灰度图像TOZERO变换
    _, gray_T = cv2.threshold(gray, 125, 255, cv2.THRESH_TOZERO)
    _, gray_T_V = cv2.threshold(gray, 125, 255, cv2.THRESH_TOZERO_INV)
    cv2.imshow('gray_T', gray_T)
    cv2.imshow('gray_T_V', gray_T_V)

    # 灰度图像TRUNC变换
    _, gray_TRUNC = cv2.threshold(gray, 125, 255, cv2.THRESH_TRUNC)
    cv2.imshow('gray_TRUNC', gray_TRUNC)

    # 灰度图像OSTU大津法和TRIANGLE三角法
    img1 = cv2.imread('threshold.png', cv2.IMREAD_GRAYSCALE)
    _, img1_O = cv2.threshold(img1, 100, 255, cv2.THRESH_BINARY|cv2.THRESH_OTSU)
    _, img1_T = cv2.threshold(img1, 125, 255, cv2.THRESH_BINARY|cv2.THRESH_TRIANGLE)
    cv2.imshow('img1_0', img1_O)
    cv2.imshow('img1_T', img1_T)

    # 灰度图像自适应二值化
    adaptive_mean = cv2.adaptiveThreshold(img1, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 13, 0)
    adaptive_gauss = cv2.adaptiveThreshold(img1, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 13, 0)
    cv2.imshow('adaptive_mean', adaptive_mean)
    cv2.imshow('adaptive_gauss', adaptive_gauss)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
