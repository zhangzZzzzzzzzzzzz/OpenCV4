import cv2
import sys
import numpy as np


def draw(event, x, y, flags, param):
    global img, pre_pts
    if event == cv2.EVENT_RBUTTONDOWN:
        print('请单击鼠标左键进行轨迹绘制')

    if event == cv2.EVENT_LBUTTONDOWN:
        pre_pts = (x, y)
        print('轨迹起始坐标为：{},{}'.format(x, y))

    if event == cv2.EVENT_MOUSEMOVE and flags == cv2.EVENT_FLAG_LBUTTON:
        img = cv2.line(img, pre_pts, (x, y), (0, 0, 255), 2, 5, 0)
        pre_pts = (x, y)
        cv2.imshow('image', img)


if __name__ == '__main__':
    img = cv2.imread('lena.jpeg')
    if img is None:
        print('Failed to read lena.jpg')
        sys.exit()
    pre_pts = -1, -1
    cv2.imshow('image', img)
    cv2.setMouseCallback('image', draw)
    cv2.waitKey(0)
    cv2.destroyAllWindows()