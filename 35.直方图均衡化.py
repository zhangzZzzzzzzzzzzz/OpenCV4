import cv2
import numpy as np
from matplotlib import pyplot as plt
import sys


if __name__ == '__main__':
    image = cv2.imread('equalizeHist.jpg', 0)
    if image is None:
        print('Failed to read image')
        sys.exit()
    # 绘制直方图
    plt.hist(image.ravel(), 256, [0, 256])
    plt.title('Origin Image')
    plt.show()
    # 进行直方图均衡化并绘制直方图
    image_result = cv2.equalizeHist(image)
    image_result = cv2.cvtColor(image_result, cv2.COLOR_GRAY2BGR)
    print(image_result.shape)
    plt.hist(image_result.ravel(), 256, [0, 256])
    plt.title('Equalized Image')
    plt.show()
    # 展示直方图均衡化前后的图像
    image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
    cv2.imshow('Origin image', image)
    print(image.shape)
    cv2.imshow('Equalized Image', image_result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()