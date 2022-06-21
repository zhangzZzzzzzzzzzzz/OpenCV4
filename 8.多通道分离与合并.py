import cv2
import sys
import numpy as np


if __name__ == '__main__':
    image = cv2.imread('lena.jpeg')
    if image is None:
        print('Failed to read lena.jpeg')
        sys.exit()
    else:
        # 通道分离
        b, g, r = cv2.split(image)

        zeros = np.zeros(image.shape[:2], np.uint8)
        # 通道合并
        bg = cv2.merge([b, g, zeros])
        gr = cv2.merge([zeros, g, r])
        br = cv2.merge([b, zeros, r])
        # 将通道数目不相同的图像矩阵进行合并
        bgr_6 = cv2.merge([bg, r, zeros, zeros])

        cv2.imshow('Blue', b)
        cv2.imshow('Green', g)
        cv2.imshow('Red', r)
        cv2.imshow('bg', bg)
        cv2.imshow('gr', gr)
        cv2.imshow('br', br)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


