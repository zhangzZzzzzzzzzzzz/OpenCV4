import cv2
import numpy as np
import sys


if __name__ == '__main__':
    array = np.array([[1, 1, 1, 1, 1],
                      [1, 1, 1, 1, 1],
                      [1, 1, 0, 1, 1],
                      [1, 1, 1, 1, 1],
                      [1, 1, 1, 1, 1]], np.uint8)
    # 分别计算街区距离、欧式距离和棋盘距离
    dst_L1 = cv2.distanceTransform(array, cv2.DIST_L1, cv2.DIST_MASK_3)
    dst_L2 = cv2.distanceTransform(array, cv2.DIST_L2, cv2.DIST_MASK_5)
    dst_C = cv2.distanceTransform(array, cv2.DIST_C, cv2.DIST_MASK_3)

    # 对图像进行读取
    rice = cv2.imread('rice.png', cv2.IMREAD_GRAYSCALE)
    if rice is None:
        print('Failed to read img')
        sys.exit()
    # 将图像转化为二值图像，同时将黑白区域颠倒
    rice_BW = cv2.threshold(rice, 50, 255, cv2.THRESH_BINARY)
    rice_BW_INV = cv2.threshold(rice, 50, 255, cv2.THRESH_BINARY_INV)

    # 图像距离变换
    dst_rice_BW = cv2.distanceTransform(rice_BW[1], 1, 3, dstType=cv2.CV_32F)
    dst_rice_INV = cv2.distanceTransform(rice_BW_INV[1], 1, 3, dstType=cv2.CV_8U)
    print(dst_rice_INV)

    print('街区距离：\n{}'.format(dst_L1))
    print('欧式距离：\n{}'.format(dst_L2))
    print('棋盘距离：\n{}'.format(dst_C))

    cv2.imshow('rice_bw', rice_BW[1])
    cv2.imshow('rice_bw_INV', rice_BW_INV[1])
    cv2.imshow('dst_rice_bw', dst_rice_BW)
    cv2.imshow('dst_rice_bw_inv', dst_rice_INV)
    cv2.waitKey(0)
    cv2.destroyAllWindows()