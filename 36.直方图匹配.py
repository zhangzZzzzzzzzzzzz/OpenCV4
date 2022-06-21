import cv2
import numpy as np
import sys
from matplotlib import pyplot as plt


if __name__ == '__main__':
    image1 = cv2.imread('Hist_Match.png')
    image2 = cv2.imread('equalLena.png')
    if image1 is None or image2 is None:
        print('Failed to read image')
        sys.exit()
    # 计算两幅图的直方图
    hist_image1 = cv2.calcHist([image1], [0], None, [256], [0, 256])
    hist_image2 = cv2.calcHist([image2], [0], None, [256], [0, 256])

    # 直方图归一化
    hist_image1 = cv2.normalize(hist_image1, None, norm_type=cv2.NORM_L1)
    hist_image2 = cv2.normalize(hist_image2, None, norm_type=cv2.NORM_L1)

    # 计算累计概率
    hist1_cdf = np.zeros((256, ))
    hist2_cdf = np.zeros((256, ))
    hist1_cdf[0] = hist_image1[0]
    hist2_cdf[0] = hist_image2[0]
    for i in range(1, 256):
        hist1_cdf[i] = hist1_cdf[i-1] + hist_image1[i]
        hist2_cdf[i] = hist2_cdf[i-1] + hist_image2[i]
    # 构建累积概率误差矩阵
    diff_cdf = np.zeros((256, 256))
    for k in range(256):
        for j in range(256):
            diff_cdf[k][j] = np.fabs((hist1_cdf[k] - hist2_cdf[j]))

    # 生成映射表
    lut = np.zeros((256, ), np.uint8)
    for m in range(256):
        min_val = diff_cdf[m][0]
        index = 0
        for n in range(256):
            if min_val > diff_cdf[m][n]:
                min_val = diff_cdf[m][n]
                index = n
        lut[m] = index
    result = cv2.LUT(image1, lut)
    cv2.imshow('Origin Image1', image1)
    cv2.imshow('Origin Image2', image2)
    cv2.imshow('Result', result)
    plt.hist(image1.ravel(), 256, [0, 256])
    plt.show()
    plt.hist(image2.ravel(), 256, [0, 256])
    plt.show()
    plt.hist(result.ravel(), 256, [0, 256])
    plt.show()
    cv2.waitKey(0)
    cv2.destroyAllWindows()