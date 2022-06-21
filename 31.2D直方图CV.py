import cv2
import numpy as np
import sys


if __name__ == '__main__':
    # 构建HSV格式的底图，然后将其转化为BGR格式
    hsv_map = np.zeros((180, 256, 3), np.uint8)
    h, s = np.indices(hsv_map.shape[:2])
    hsv_map[:, :, 0] = h
    hsv_map[:, :, 1] = s
    hsv_map[:, :, 2] = 255
    hsv_map = cv2.cvtColor(hsv_map, cv2.COLOR_HSV2BGR)

    image = cv2.imread('road.jpg')
    if image is None:
        print('Failed to read img.jpg')
        sys.exit()
    image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    # 计算2D直方图
    image_hist = cv2.calcHist([image_hsv], [0, 1], None, [180, 256], [0, 180, 0, 256])
    # 将计算出的直方图矩阵和创建的hsv_map相乘
    print('2D直方图计算结果：\n{}'.format(image_hist))
    image_hist = np.clip(image_hist * 0.05, 0, 1)
    result = hsv_map * image_hist[:, :, np.newaxis] / 255.0

    cv2.imshow('Origin Image', image)
    cv2.imshow('Hsv Map', hsv_map)
    cv2.imshow('2D hist', result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

