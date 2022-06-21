# 同时对X、Y方向检测
import cv2
import sys


if __name__ == '__main__':
    image = cv2.imread('equalLena.png')
    if image is None:
        print('Failed to read img')
        sys.exit()
    # 通过高阈值检测图像边缘
    result_high = cv2.Canny(image, 100, 200, apertureSize=3)
    # 通过低阈值检测图像边缘
    result_low = cv2.Canny(image, 20, 40, apertureSize=3)
    # 高斯模糊后检测图像
    result_gauss = cv2.GaussianBlur(image, (3, 3), 5)
    result_gauss = cv2.Canny(result_gauss, 100, 200, apertureSize=3)

    cv2.imshow('result_high', result_high)
    cv2.imshow('result_low', result_low)
    cv2.imshow('result_gauss', result_gauss)
    cv2.waitKey(0)
    cv2.destroyAllWindows()