import cv2
import numpy as np
from matplotlib import pyplot as plt
import sys


if __name__ == '__main__':
    # 对数组进行归一化
    data = np.array([2.0, 8.0, 10.0])
    # 绝对值求和归一化
    data_L1 = cv2.normalize(data, None, 1.0, 0.0, cv2.NORM_L1)
    # 模长归一化
    data_L2 = cv2.normalize(data, None, 1.0, 0.0, cv2.NORM_L2)
    # 最大值归一化
    data_Inf = cv2.normalize(data, None, 1.0, 0.0, cv2.NORM_INF)
    # 线性归一化
    data_MINMAX = cv2.normalize(data, None, 0.0, 1.0, cv2.NORM_MINMAX)
    # 展示结果
    print('绝对值求和归一化结果为\n{}'.format(data_L1))
    print('模长归一化结果为\n{}'.format(data_L2))
    print('最大值归一化结果为\n{}'.format(data_Inf))
    print('线性归一化结果为\n{}'.format(data_MINMAX))

    # 对直方图进行归一化
    # 读取图像
    image = cv2.imread('apple.jpg')
    if image is None:
        print('Failed to read image')
        sys.exit()
    # 将图像转化为灰度图
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # 对图像进行直方图计算
    hist_item = cv2.calcHist([gray_image], [0], None, [256], [0, 256])
    # 对直方图进行绝对值求和归一化
    image_L1 = cv2.normalize(hist_item, None, 1, 0, cv2.NORM_L1)
    # 对直方图进行最大值归一化
    image_L2 = cv2.normalize(hist_item, None, 1, 0, cv2.NORM_INF)

    plt.plot(image_L1)
    plt.show()
    plt.plot(image_L2)
    plt.show()
