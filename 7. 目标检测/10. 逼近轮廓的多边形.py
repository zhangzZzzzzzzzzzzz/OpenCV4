import cv2
import sys
import numpy as np


def judge_shape(val):
    if val == 3:
        return 'Triangle'
    if val == 4:
        return 'Rectangle'
    else:
        return 'Polygon-{}'.format(val)


if __name__ == '__main__':
    image = cv2.imread('approx.png')
    # 提取图像的边缘
    canny = cv2.Canny(image, 80, 160, 3)
    # 膨胀运算
    kernel = cv2.getStructuringElement(0, (3, 3))
    canny = cv2.dilate(canny, kernel=kernel)
    # 轮廓检测及绘制
    contours, hierarchy = cv2.findContours(canny, mode=0, method=2)

    for i in range(len(contours)):
        # 多边形拟合
        approx = cv2.approxPolyDP(contours[i], 4, closed=True)
        print(approx.shape)
        # 多边形绘制
        image = cv2.drawContours(image, [approx], -1, (0, 255, 0), 2, 8)
        # 计算并绘制多边形中心
        center = np.int0((sum(approx))[0] / len(approx))
        center = (center[0], center[1])
        cv2.circle(image, center, 3, (0, 0, 255), -1)
        cv2.putText(image, text=judge_shape(approx.shape[0]), org=center, fontFace=1, fontScale=1, color=
                    (0, 0, 255))
    cv2.imshow('Approx', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()