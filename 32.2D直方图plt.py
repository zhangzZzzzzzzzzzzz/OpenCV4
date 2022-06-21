import cv2
from matplotlib import pyplot as plt
import numpy
import sys

if __name__ == '__main__':
    image = cv2.imread('road.jpg')
    if image is None:
        print('Failed to read image')
        sys.exit()
    # 将图像从BGR转化为HSV
    image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    # 计算2D直方图
    image_hist = cv2.calcHist([image_hsv], [0, 1], None, [180, 256], [0, 180, 0, 256])

    cv2.imshow('Origin Image', image)
    plt.imshow(image_hist, interpolation='nearest')
    plt.show()
    cv2.waitKey(0)
    cv2.destroyAllWindows()