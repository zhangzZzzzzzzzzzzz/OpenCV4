import cv2
import numpy as np
import sys


if __name__ == '__main__':
    image = cv2.imread('equalLena.png')
    if image is None:
        print('Failed to read img')
        sys.exit()
    # x方向一阶Sobel算子
    result_X = cv2.Sobel(image, cv2.CV_16S, 1, 0, 3)
    result_X1 = cv2.Sobel(image, cv2.CV_16S, 2, 0)
    result_X = cv2.convertScaleAbs(result_X)
    result_X1 = cv2.convertScaleAbs(result_X1)
    # y方向一阶边缘
    result_Y = cv2.Sobel(image, cv2.CV_16S, 0, 1, 3)
    result_Y = cv2.convertScaleAbs(result_Y)
    # 整幅图像的Sobel检测边缘
    res = result_X + result_Y

    cv2.imshow('resX', result_X)
    cv2.imshow('resx1',result_X1)
    cv2.imshow('resY', result_Y)
    cv2.imshow('res', res)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
