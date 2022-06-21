# 同时对X、Y方向检测
import cv2
import sys


if __name__ == '__main__':
    image = cv2.imread('equalLena.png')
    if image is None:
        print('Failed to read img')
        sys.exit()
    # 未滤波利用拉普拉斯算子边缘检测
    result = cv2.Laplacian(image, cv2.CV_16S, ksize=3)
    result = cv2.convertScaleAbs(result)
    # 先利用高斯滤波再进行拉普拉斯算子边缘检测
    result_gauss = cv2.GaussianBlur(image, (3, 3), 5, 0)
    result_gauss = cv2.Laplacian(result_gauss, cv2.CV_16S, ksize=3)
    result_gauss = cv2.convertScaleAbs(result_gauss)

    cv2.imshow('result', result)
    cv2.imshow('result_gauss', result_gauss)
    cv2.waitKey(0)
    cv2.destroyAllWindows()