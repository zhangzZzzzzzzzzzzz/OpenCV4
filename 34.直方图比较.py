import cv2
import numpy as np
import sys
from matplotlib import pyplot as plt


def normalize_image(path):
    image = cv2.imread(path, 0)
    if image is None:
        print('Failed to read image')
        sys.exit()
    # 绘制直方图
    plt.hist(image.ravel(), 256, [0, 256])
    plt.title(path.split('.'[0]))
    plt.show()
    # 计算直方图
    hist_item = cv2.calcHist([image], [0], None, [256], [0, 256])
    print(hist_item.shape)
    # 进行归一化
    imgage_nor = cv2.normalize(hist_item, None, 0, 1, cv2.NORM_MINMAX)
    # normalize_result = np.zeros(hist_item.shape, np.float32)
    # cv2.normalize(hist_item, normalize_result, 0, 1, cv2.NORM_MINMAX)
    return imgage_nor


def compare_hist(image1_path, image2_path):
    image1 = normalize_image(image1_path)
    image2 = normalize_image(image2_path)
    # 进行直方图比较
    return round(cv2.compareHist(image1, image2, cv2.HISTCMP_CORREL), 2)


if __name__ == '__main__':
    img1_path = 'Compare_Hist_1.jpg'
    img2_path = 'Compare_Hist_2.jpg'
    img3_path = 'Compare_Hist_3.jpg'
    img4_path = 'Compare_Hist_4.jpg'
    print('Compare_Hist_1.jpg与Compare_Hist_2.jpg的相似性%s' % (compare_hist(img1_path, img2_path)))
    print('Compare_Hist_3.jpg与Compare_Hist_4.jpg的相似性%s' % (compare_hist(img3_path, img4_path)))