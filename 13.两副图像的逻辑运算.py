import cv2
import numpy as np
import sys

if __name__ == '__main__':
    # 创建两幅黑白图像
    img1 = np.zeros((200, 200), dtype='uint8')
    img2 = np.zeros((200, 200), dtype='uint8')
    img1[50:150, 50:150] = 255
    img2[100:200, 100:200] = 255
    # 读取图像
    img = cv2.imread('lena.jpeg')
    if img is None:
        print('Failed to read lena.jpg')
        sys.exit()

    # 进行逻辑运算
    Not = cv2.bitwise_not(img1)
    And = cv2.bitwise_and(img1, img2)
    Or = cv2.bitwise_or(img1, img2)
    Xor = cv2.bitwise_xor(img1, img2)
    Img_Not = cv2.bitwise_not(img)

    cv2.imshow('img1', img1)
    cv2.imshow('img2', img2)
    cv2.imshow('Not', Not)
    cv2.imshow('And', And)
    cv2.imshow('Or', Or)
    cv2.imshow('Xor', Xor)
    cv2.imshow('Img', img)
    cv2.imshow('Img_Not', Img_Not)

    cv2.waitKey(0)
    cv2.destroyAllWindows()