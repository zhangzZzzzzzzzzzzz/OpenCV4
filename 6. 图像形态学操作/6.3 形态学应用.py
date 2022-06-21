import cv2
import numpy as np


if __name__ == '__main__':
    src = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 255, 255, 255, 255, 255, 255, 255, 0, 0, 255, 0],
                    [0, 255, 255, 255, 255, 255, 255, 255, 0, 0, 0, 0],
                    [0, 255, 255, 255, 255, 255, 255, 255, 0, 0, 0, 0],
                    [0, 255, 255, 255, 0, 255, 255, 255, 0, 0, 0, 0],
                    [0, 255, 255, 255, 255, 255, 255, 255, 0, 0, 0, 0],
                    [0, 255, 255, 255, 255, 255, 255, 255, 0, 0, 255, 0],
                    [0, 255, 255, 255, 255, 255, 255, 255, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]], np.uint8)
    kernel = cv2.getStructuringElement(0, (3, 3))
    # 对二值矩阵分别进行开运算、闭运算、形态学梯度、顶帽运算、 黑帽运算、击中击不中变换
    open_src = cv2.morphologyEx(src, cv2.MORPH_OPEN, kernel)
    close_src = cv2.morphologyEx(src, cv2.MORPH_CLOSE, kernel)
    gradient_src = cv2.morphologyEx(src, cv2.MORPH_GRADIENT, kernel)
    tophat_src = cv2.morphologyEx(src, cv2.MORPH_TOPHAT, kernel)
    blackhat_src = cv2.morphologyEx(src, cv2.MORPH_BLACKHAT, kernel)
    hitmiss_src = cv2.morphologyEx(src, cv2.MORPH_HITMISS, kernel)
    cv2.namedWindow('src', cv2.WINDOW_NORMAL)
    cv2.imshow('src', src)
    cv2.namedWindow('open', cv2.WINDOW_NORMAL)
    cv2.imshow('open', open_src)
    cv2.namedWindow('close', cv2.WINDOW_NORMAL)
    cv2.imshow('close', close_src)
    cv2.namedWindow('grd', cv2.WINDOW_NORMAL)
    cv2.imshow('grd', gradient_src)
    cv2.namedWindow('top', cv2.WINDOW_NORMAL)
    cv2.imshow('top', tophat_src)
    cv2.namedWindow('black', cv2.WINDOW_NORMAL)
    cv2.imshow('black', blackhat_src)
    cv2.namedWindow('hit', cv2.WINDOW_NORMAL)
    cv2.imshow('hit', hitmiss_src)


    keys = cv2.imread('keys.jpg', cv2.IMREAD_GRAYSCALE)
    cv2.imshow('Origin', keys)
    keys = cv2.threshold(keys, 130, 255, cv2.THRESH_BINARY)[1]
    kernel_keys = cv2.getStructuringElement(0, (5, 5))
    # 对图像分别进行开运算、闭运算、形态学梯度、顶帽运算、 黑帽运算、击中击不中变换
    open_keys = cv2.morphologyEx(keys, cv2.MORPH_OPEN, kernel_keys)
    close_keys = cv2.morphologyEx(keys, cv2.MORPH_CLOSE, kernel_keys)
    gradient_keys = cv2.morphologyEx(keys, cv2.MORPH_GRADIENT, kernel_keys)
    tophat_keys = cv2.morphologyEx(keys, cv2.MORPH_TOPHAT, kernel_keys)
    blackhat_keys = cv2.morphologyEx(keys, cv2.MORPH_BLACKHAT, kernel_keys)
    hitmiss_keys = cv2.morphologyEx(keys, cv2.MORPH_HITMISS, kernel_keys)
    cv2.namedWindow('keys', cv2.WINDOW_NORMAL)
    cv2.imshow('keys', keys)
    cv2.namedWindow('open_k', cv2.WINDOW_NORMAL)
    cv2.imshow('open_k', open_keys)
    cv2.namedWindow('close_k', cv2.WINDOW_NORMAL)
    cv2.imshow('close_k', close_keys)
    cv2.namedWindow('grd_k', cv2.WINDOW_NORMAL)
    cv2.imshow('grd_k', gradient_keys)
    cv2.namedWindow('top_k', cv2.WINDOW_NORMAL)
    cv2.imshow('top_k', tophat_keys)
    cv2.namedWindow('black_k', cv2.WINDOW_NORMAL)
    cv2.imshow('black_k', blackhat_keys)
    cv2.namedWindow('hit_k', cv2.WINDOW_NORMAL)
    cv2.imshow('hit_k', hitmiss_keys)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

