import cv2
import numpy as np
import sys


def call_back1_brightness(x):
    global value, img, img1
    value = cv2.getTrackbarPos('brightness', 'Brighter')
    img1 = np.uint8(np.clip((value/100*img), 0, 255))


if __name__ == '__main__':
    # 读取图像并判断是否成功
    img = cv2.imread('lena.jpeg')
    img1 = img.copy()
    if img is None:
        print('Failed to read lena.jpg')
        sys.exit()
    cv2.namedWindow('Brighter')
    # 设置滑动窗口的初始值
    value = 100
    cv2.createTrackbar('brightness', 'Brighter', value, 300, call_back1_brightness)
    while True:
        cv2.imshow('Brighter', img1)
        if cv2.waitKey(1) == ord('q'):
            break
    cv2.destroyAllWindows()
