import cv2
import sys


if __name__ == '__main__':
    origin_image = cv2.imread('calcBackProject.jpg')
    template_image = cv2.imread('calcBackProject_template.jpg')
    if origin_image is None or template_image is None:
        print('Failed to read image')
    # 转化到HSV色彩空间
    origin_image_hsv = cv2.cvtColor(origin_image, cv2.COLOR_BGR2HSV)
    template_image_hsv = cv2.cvtColor(template_image, cv2.COLOR_BGR2HSV)
    # 计算模板直方图
    template_image_hist = cv2.calcHist([template_image_hsv], [0, 1], None, [180, 256], [0, 180, 0, 256])
    # 直方图归一化
    template_image_hist = cv2.normalize(template_image_hist, None, 0, 255, norm_type=cv2.NORM_MINMAX)
    # 直方图反向投影
    result = cv2.calcBackProject([origin_image_hsv], [0, 1], template_image_hist, [0, 180, 0, 256], 1)
    cv2.imshow('Origin Image', origin_image)
    cv2.imshow('Template Image', template_image)
    cv2.imshow('result', result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()