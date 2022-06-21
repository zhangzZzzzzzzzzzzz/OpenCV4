import cv2
import sys


if __name__ == '__main__':
    img1 = cv2.imread('face1.png')
    img2 = cv2.imread('face2.png')
    if img1 is None or img2 is None:
        print('Failed to read img')
        sys.exit()
    # 验证不同滤波器直径的滤波效果
    res1 = cv2.bilateralFilter(img1, 9, 50, 25/2)
    res2 = cv2.bilateralFilter(img1, 25, 50, 25/2)

    # 验证不同标准差的滤波效果
    res3 = cv2.bilateralFilter(img2, 9, 9, 9)
    res4 = cv2.bilateralFilter(img2, 9, 200, 200)

    cv2.imshow('Origin Image1', img1)
    cv2.imshow('Origin Image2', img2)
    cv2.imshow('res1', res1)
    cv2.imshow('res2', res2)
    cv2.imshow('res3', res3)
    cv2.imshow('res4', res4)
    cv2.waitKey(0)
    cv2.destroyAllWindows()