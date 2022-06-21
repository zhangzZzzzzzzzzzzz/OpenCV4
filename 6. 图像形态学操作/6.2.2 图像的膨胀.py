import cv2
import numpy as np
import sys


if __name__ == '__main__':
    image = np.array([[0, 0, 0, 0, 255, 0],
                      [0, 255, 255, 255, 255, 255],
                      [0, 255, 255, 255, 255, 0],
                      [0, 255, 255, 255, 255, 0],
                      [0, 255, 255, 255, 255, 0],
                      [0, 0, 0, 0, 0, 0]], np.uint8)
    black = cv2.imread('LearnCV_black.png', cv2.IMREAD_GRAYSCALE)
    white = cv2.imread('LearnCV_white.png', cv2.IMREAD_GRAYSCALE)
    # 生成结构元
    structure1 = cv2.getStructuringElement(0, (3, 3))
    structure2 = cv2.getStructuringElement(1, (3, 3))
    # 对图像进行膨胀操作
    dilate_image = cv2.dilate(image, structure2)
    dilate_black_1 = cv2.dilate(black, structure1)
    dilate_black_2 = cv2.dilate(black, structure2)
    dilate_white_1 = cv2.dilate(white, structure1)
    dilate_white_2 = cv2.dilate(white, structure2)
    erode_black = cv2.erode(black, structure1)
    result_xor = cv2.bitwise_xor(erode_black, dilate_white_1)
    result_and = cv2.bitwise_and(erode_black, dilate_white_1)

    cv2.namedWindow('image', cv2.WINDOW_NORMAL)
    cv2.namedWindow('dilate_image', cv2.WINDOW_NORMAL)
    cv2.imshow('image', image)
    cv2.imshow('dilate_image', dilate_image)
    cv2.imshow('black', black)
    cv2.imshow('dilate_black_1', dilate_black_1)
    cv2.imshow('dilate_black_2', dilate_black_2)
    cv2.imshow('white', white)
    cv2.imshow('dilate_white_1', dilate_white_1)
    cv2.imshow('dilate_white_2', dilate_white_2)
    cv2.imshow('result_Xor', result_xor)
    cv2.imshow('result_and', result_and)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
