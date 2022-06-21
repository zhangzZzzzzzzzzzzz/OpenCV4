import cv2
import sys


if __name__ == '__main__':
    image = cv2.imread('approx.png')
    if image is None:
        print('Failed to read img')
        sys.exit()

    # 灰度化
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # 二值化
    _, binary = cv2.threshold(gray, 105, 255, cv2.THRESH_BINARY)
    # 对图像进行开运算
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (9, 9), (-1, -1))
    binary = cv2.morphologyEx(binary, cv2.MORPH_OPEN, kernel)
    # 轮廓检测
    contours, hierarchy = cv2.findContours(binary, mode=cv2.RETR_TREE, method=cv2.CHAIN_APPROX_SIMPLE)
    for i in contours:
        M = cv2.moments(i)
        print('Spatial moments:')
        print('m00:{}, m10:{}, m01:{}, m20:{}, m11:{}'.format(M['m00'], M['m10'], M['m01'], M['m20'], M['m11']))
