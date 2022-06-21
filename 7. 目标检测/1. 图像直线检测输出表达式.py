# 霍夫变换检测直线
import cv2
import numpy as np
import sys


def draw_line(img, lines):
    img_copy = img.copy()
    for i in range(0, len(lines)):
        rho, theta = lines[i][0][0], lines[i][0][1]
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = rho * a
        y0 = rho * b
        x1 = int(x0 + 1000*(-b))
        y1 = int(y0 + 1000*a)
        x2 = int(x0 - 1000*(-b))
        y2 = int(y0 - 1000*a)
        cv2.line(img_copy, (x1, y1), (x2, y2), (255, 255, 255), 2)
    return img_copy


if __name__ == '__main__':
    image = cv2.imread('HoughLines.jpg')
    if image is None:
        print('Failed to read img')
        sys.exit()
    cv2.imshow('Origin Image', image)
    # 检测图像边缘
    image_edge = cv2.Canny(image, 50, 150, 3)
    cv2.imshow('image_edge', image_edge)

    # 分别设置不同累加器阈值进行直线检测
    threshold_1 = 200
    lines_1 = cv2.HoughLines(image_edge, 1, np.pi / 180, threshold_1)
    print(lines_1.shape)
    try:
        img1 = draw_line(image, lines_1)
        cv2.imshow('Image HoughLines({})'.format(threshold_1), img1)
    except TypeError:
        print('累加器阈值设为{}时，不能检测出直线'.format(threshold_1))

    threshold_2 = 300
    lines_2 = cv2.HoughLines(image_edge, 1, np.pi / 180, threshold_2)
    try:
        img2 = draw_line(image, lines_2)
        cv2.imshow('Image HouguLines({})'.format(threshold_2), img2)
    except TypeError:
        print('累加器阈值设为{}时，不能检测出直线'.format(threshold_2))

    cv2.waitKey(0)
    cv2.destroyAllWindows()
