# 寻找2D点集的最小包围三角形、圆形
import cv2
import numpy as np


if __name__ == '__main__':
    # 生成空白图像
    image = np.zeros((500, 500))
    # 生成随机点
    points = np.random.randint(150, 270, [100, 2]).astype('float32')
    # 在图像上绘制随机点
    for pt in points:
        cv2.circle(image, (int(pt[0]), int(pt[1])), 1, (255, 255, 255), -1)
    image1 = image.copy()
    # 寻找包围点集的三角形
    triangle = cv2.minEnclosingTriangle(points)
    # 寻找包围点集的圆形
    center, radius = cv2.minEnclosingCircle(points)
    # 绘制三角形
    triangle = triangle[1]
    a = triangle[0][0]
    a = np.int0(a)
    b = triangle[1][0]
    b = np.int0(b)
    c = triangle[2][0]
    c = np.int0(c)
    cv2.line(image, (a[0], a[1]), (b[0], b[1]), (255, 255, 255), 1, 16)
    cv2.line(image, (a[0], a[1]), (c[0], c[1]), (255, 255, 255), 1, 16)
    cv2.line(image, (b[0], b[1]), (c[0], c[1]), (255, 255, 255), 1, 16)
    # 绘制圆形
    center = np.int0(center)             # 转化为整数
    cv2.circle(image1, (center[0], center[1]), int(radius), (255, 255, 255), 1, cv2.LINE_AA)
    cv2.imshow('Triangle', image)
    cv2.imshow('Circle', image1)
    cv2.waitKey(0)
    cv2.destroyAllWindows()