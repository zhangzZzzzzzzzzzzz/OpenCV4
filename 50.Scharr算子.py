import cv2
import numpy as np
import sys


if __name__ == '__main__':
    image = cv2.imread('equalLena.png')
    if image is None:
        print('Failed to read img')
        sys.exit()
    # x方向的一阶边缘
    result_X = cv2.Scharr(image, cv2.CV_16S, 1, 0)
    result_X = cv2.convertScaleAbs(result_X)
    # y方向的一阶边缘
    result_Y = cv2.Scharr(image, cv2.CV_16S, 0, 1)
    result_Y = cv2.convertScaleAbs(result_Y)
    # 整幅图像的边缘
    res = result_X +  result_Y
    cv2.imshow('resX', result_X)
    cv2.imshow('resY', result_Y)
    cv2.imshow('res', res)
    cv2.waitKey(0)
    cv2.destroyAllWindows()