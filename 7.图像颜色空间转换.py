import cv2
import sys
import numpy as np


if __name__ == '__main__':
    img = cv2.imread('lena.jpeg')
    if img is None:
        print('Failed to read lena.jpg')
        sys.exit()
    else:
        # 将图像进行颜色空间转换
        image = img.astype('float32')
        print(image[30, 30])
        image *= 1.0/255
        HSV = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        YUV = cv2.cvtColor(image, cv2.COLOR_BGR2YUV)
        Lab = cv2.cvtColor(image, cv2.COLOR_BGR2Lab)
        Gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        cv2.imshow('Origin image', image)
        cv2.imshow('HSV', HSV)
        cv2.imshow('YUV', YUV)
        cv2.imshow('Lab', Lab)
        cv2.imwrite('Convert Lab image.jpg', Lab)
        cv2.imshow('Gray', Gray)

        cv2.waitKey(0)
        cv2.destroyAllWindows()
