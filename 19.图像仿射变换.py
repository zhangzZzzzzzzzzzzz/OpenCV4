import cv2
import numpy as np
import sys


if __name__ == '__main__':
    img = cv2.imread('lena.jpeg')
    if img is None:
        print('Failed to read lena.jpg')
        sys.exit()
    # 设置图像旋转中心点、角度、尺度变化
    angle = 30
    h, w = img.shape[:-1]
    size = (w, h)
    center = (w/2.0, h/2.0)
    # 计算仿射变换矩阵
    rotation0 = cv2.getRotationMatrix2D(center, angle, 1)
    # 进行仿射变换
    img_warp0 = cv2.warpAffine(img, rotation0, size)

    # 根据定义的3个对应点坐标进行仿射变换
    src_points = np.array([[0, 0], [0, h-1], [w-1, h-1]], dtype='float32')
    dst_points = np.array([[w*0.11, h*0.2], [w*0.15, h*0.7], [w*0.81, h*0.85]], dtype='float32')
    rotation1 = cv2.getAffineTransform(src_points, dst_points)
    img_warp1 = cv2.warpAffine(img, rotation1, size)

    cv2.imshow('img_warp0', img_warp0)
    cv2.imshow('img_warp1', img_warp1)
    cv2.waitKey(0)
    cv2.destroyAllWindows()