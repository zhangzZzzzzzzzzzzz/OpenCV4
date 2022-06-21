import cv2
import random
import numpy as np
import sys


def add_noise(image, n=10000):
    result = image.copy()
    w, h = image.shape[:2]
    for i in range(n):
        x = np.random.randint(1, w)
        y = np.random.randint(1, h)
        if np.random.randint(0, 2) == 1:
            result[x, y] = 255
        else:
            result[x, y] = 0
    return result


if __name__ == '__main__':
    img = cv2.imread('dolphins.jpg')
    if img is None:
        print('Failed to read img')
        sys.exit()
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # 为灰度图像添加椒盐噪声
    result1 = add_noise(gray_img, 10000)
    # 彩色图像添加椒盐噪声
    result2 = add_noise(img, 10000)
    cv2.imshow('Origin_Gray Image', gray_img)
    cv2.imshow('Origin_Gray_Noise Image', result1)
    cv2.imshow('Origin_RGB Image', img)
    cv2.imshow('Origin_RGB_Noise Image', result2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()