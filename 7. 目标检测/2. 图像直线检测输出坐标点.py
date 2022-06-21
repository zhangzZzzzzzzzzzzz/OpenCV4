import cv2
import numpy as np
import sys


def draw_line(img, lines):
    img_copy = img.copy()
    for i in range(0, len(lines)):
        for x1, y1, x2, y2 in lines[i]:
            cv2.line(img_copy, (x1, y1), (x2, y2), (255, 255, 255), 2)
        #cv2.line(img_copy, (int(lines[i][0][0]), int(lines[i][0][1])), (int(lines[i][0][2]), int(lines[i][0][3])),
                 #(255, 255, 255), 2)
    return img_copy


if __name__ == '__main__':
    image = cv2.imread('HoughLines.jpg')
    if image is None:
        print('failed to read img')
        sys.exit()
    cv2.imshow('Origin img', image)
    # 提取图像边缘
    image_edge = cv2.Canny(image, 80, 180, 3)
    cv2.imshow('Image edge', image_edge)
    # 设置线段的最小长度
    min_line_length = 200
    # 分别设置不同最大连接距离并进行直线检测
    max_line_gap_1 = 5
    line_1 = cv2.HoughLinesP(image_edge, 1, np.pi/180, 150, minLineLength=min_line_length, maxLineGap=max_line_gap_1)
    try:
        img1 = draw_line(image, line_1)
        cv2.imshow('Image HoughLineP({})'.format(max_line_gap_1), img1)
    except TypeError:
        print('最大连接距离设为{}时，不能检测出直线。'.format(max_line_gap_1))
    print(line_1)
    max_line_gap_2 = 20
    line_2 = cv2.HoughLinesP(image_edge, 1, np.pi/180, 150, minLineLength=min_line_length, maxLineGap=max_line_gap_2)
    try:
        img2 = draw_line(image, line_2)
        cv2.imshow('Image HoughLineP({})'.format(max_line_gap_2), img2)
    except TypeError:
        print('最大连接距离设为{}时，不能检测出直线。'.format(max_line_gap_2))

    cv2.waitKey(0)
    cv2.destroyAllWindows()