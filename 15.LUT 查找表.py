import cv2
import numpy as np
import sys


if __name__ == '__main__':
    # LUT第一层
    LUT_1 = np.zeros(256, dtype='uint8')
    LUT_1[101:201] = 100
    LUT_1[201:] = 255
    # LUT第二层
    LUT_2 = np.zeros(256, dtype='uint8')
    LUT_2[101:151] = 100
    LUT_2[151:201] = 150
    LUT_2[201:] = 255
    # LUT第三层
    LUT_3 = np.zeros(256, dtype='uint8')
    LUT_3[0:101] = 100
    LUT_3[101:201] = 200
    LUT_3[201:] = 255
    # 合并三通道
    LUT = cv2.merge((LUT_1, LUT_2, LUT_3))
    # 读取图像
    img = cv2.imread('lena.jpeg')
    if img is None:
        print('Failed to read lena.jpg')
        sys.exit()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    out0 = cv2.LUT(img, LUT_1)
    out1 = cv2.LUT(gray, LUT_1)
    out2 = cv2.LUT(img, LUT)
    cv2.imshow('out0', out0)
    cv2.imshow('out1', out1)
    cv2.imshow('out2', out2)
    print(out0.shape)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
