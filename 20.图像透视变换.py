import cv2
import sys
import numpy as np


if __name__ == '__main__':
    img = cv2.imread('noobcvqr.png')
    if img is None:
        print('Failed to read noobcvqr.png')
        sys.exit()
    print(img.shape)
    h, w = img.shape[:-1]
    print(h)
    size = (w, h)

    # 读取透视变换前4个角点的坐标
    with open('noobcvqr_points.txt', 'r') as f:
        src_points = np.array([tx.split(' ') for tx in f.read().split('\n')], dtype='float32')
    # 设置透视变换后的4个角点的坐标
    max_pt = np.max(src_points)
    dst_points = np.array([[0.0, 0.0], [max_pt, 0.0], [0.0, max_pt], [max_pt, max_pt]], dtype='float32')

    # 计算透视变换矩阵
    rotation = cv2.getPerspectiveTransform(src_points, dst_points)
    # 透视变换投影
    img0 = cv2.warpPerspective(img, rotation, size)

    cv2.imshow('Origin', img)
    cv2.imshow('img_warp', img0)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
