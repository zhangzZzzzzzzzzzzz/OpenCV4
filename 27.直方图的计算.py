import cv2
import sys
import numpy as np


# 不使用科学记数法，显示
np.set_printoptions(suppress=True)


if __name__ == '__main__':
    img = cv2.imread('apple.jpg')
    if img is None:
        print('Failed to read lena.jpe')
        sys.exit()
    # 对图像进行直方图的计算
    hist = cv2.calcHist([img], [0], None, [256], [0, 256])
    print(hist.shape)
    print('统计灰度的直方图\n{}'.format(hist))
