import cv2
import numpy as np


if __name__ == '__main__':
    # 新建array
    img = np.array([3, 2, 3, 4, 5, 10, 6, 7, 8, 9, 10, 5])
    # 将array调整为维度为3*4的单通道图像
    img1 = img.reshape((3, 4))
    print(img1)
    minval_1, maxval_1, minloc_1, maxloc_1 = cv2.minMaxLoc(img1)
    print('图像img1中最小值为%s,其位置为%s' % (minval_1, minloc_1))
    print('图像img1中最小值为%s,其位置为%s' % (maxval_1, maxloc_1))

    # 将array重塑为3*2*2的多通道图像
    img2 = img.reshape((3, 2, 2))
    # 将多通道重塑
    img2_re = img2.reshape((1, -1))
    print(img2_re.shape)
    minval_2, maxval_2, minloc_2, maxloc_2 = cv2.minMaxLoc(img2_re)
    print('图像img2中最小值为%s,其位置为%s' % (minval_2, minloc_2))
    print('图像img2中最小值为%s,其位置为%s' % (maxval_2, maxloc_2))



