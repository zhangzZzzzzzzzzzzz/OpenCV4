import cv2
import numpy as np
import sys


if __name__ == '__main__':
    img = cv2.imread('dial.png')
    if img is None:
        print('Failed to read dial.png')
        sys.exit()
    h, w = img.shape[:-1]
    center = (w/2, h/2)
    # 极坐标正变换
    img_res = cv2.warpPolar(img, (300, 600), center, center[0], cv2.INTER_LINEAR + cv2.WARP_POLAR_LINEAR)

    # 极坐标逆变换
    img_res1 = cv2.warpPolar(img_res, (w, h), center, center[0], cv2.INTER_LINEAR + cv2.WARP_POLAR_LINEAR +
                             cv2.WARP_INVERSE_MAP)
    cv2.imshow('Origin', img)
    cv2.imshow('img_res', img_res)
    cv2.imshow('img_res1', img_res1)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
