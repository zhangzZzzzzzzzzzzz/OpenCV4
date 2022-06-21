import cv2
import sys


if __name__ == '__main__':
    img1 = cv2.imread('LearnCV_black.png', cv2.IMREAD_GRAYSCALE)
    img2 = cv2.imread('OpenCV_4.1.png', cv2.IMREAD_GRAYSCALE)
    # 图像细化
    thin1 = cv2.ximgproc.thinning(img1, thinningType=0)
    thin2 = cv2.ximgproc.thinning(img2, thinningType=0)
    cv2.imshow('img1', img1)
    cv2.imshow('img1_thinning', thin1)
    cv2.imshow('img2', img2)
    cv2.imshow('img2_thinning', thin2)
    cv2.waitKey(0)
    cv2.destroyALLWindows()

