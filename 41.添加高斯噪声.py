import cv2
import numpy as np


def gauss_noisy(image, mean=0, val=0.01):
    size = image.shape
    image = image/255
    gauss = np.random.normal(mean, val ** 0.5, size)
    noise = image + gauss
    return gauss, noise


if __name__ == '__main__':
    img = cv2.imread('dolphins.jpg')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # 灰度图添加高斯噪声
    gauss_gray, gray_noise = gauss_noisy(gray, 0, 0.01)
    # 彩色图添加高斯噪声
    Color_gauss, Color_noise = gauss_noisy(img, 0, 0.01)
    cv2.imshow('Origin_gray', gray)
    cv2.imshow('Gray_noise', gray_noise)
    cv2.imshow('Gray_gauss', gauss_gray)
    cv2.imshow('Origin_color', img)
    cv2.imshow('Color_noise', Color_gauss)
    cv2.imshow('Color_gauss', Color_noise)
    cv2.waitKey(0)
    cv2.destroyAllWindows()