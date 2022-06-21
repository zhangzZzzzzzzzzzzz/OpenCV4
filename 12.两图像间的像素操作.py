import cv2
import numpy as np


if __name__ == '__main__':
    # 新建a和b
    a = np.array([1, 2, 3.3, 4, 5, 9, 5, 7, 8.2, 9, 10, 2])
    b = np.array([1, 2.2, 3, 1, 3, 10, 6, 7, 8, 9.3, 10, 1])
    img1 = a.reshape(3, 4)
    img2 = np.reshape(b, (3, 4))
    img3 = np.reshape(a, (2, 3, 2))
    img4 = np.reshape(b, (2, 3, 2))
    # 对两幅单通道图像进行比较
    max12 = cv2.max(img1, img2)
    min12 = cv2.min(img1, img2)
    print('max12:\n{}'.format(max12))
    print('min12:\n{}'.format(min12))

    # 对两幅彩色图像进行比较
    max34 = cv2.max(img3, img4)
    min34 = cv2.min(img3, img4)
    print('max34:\n{}'.format(max34))
    print('min34:\n{}'.format(min34))

    # 对两幅多彩图像进行比较
    img5 = cv2.imread('lena.jpeg')
    img6 = cv2.imread('lona.jpeg')
    max56 = cv2.max(img5, img6)
    min56 = cv2.min(img5, img6)
    cv2.imshow('max56', max56)
    cv2.imshow('min56', min56)

    # 对两幅灰度图像进行比较
    img7 = cv2.cvtColor(img5, cv2.COLOR_BGR2GRAY)
    img8 = cv2.cvtColor(img6, cv2.COLOR_BGR2GRAY)
    max78 = cv2.max(img7, img8)
    min78 = cv2.min(img7, img8)
    cv2.imshow('max78', max78)
    cv2.imshow('min78', min78)

    # 与掩模比较
    # 生成1个300*300的低通掩模矩阵
    src = np.zeros((512, 512, 3), np.uint8)
    src[100:400:, 100:400] = 255
    min_img5_src = cv2.min(src, img5)
    cv2.imshow('min_img5_src', min_img5_src)

    # 生成一个显示红色通道的低通淹模
    src1 = np.zeros((512, 512, 3), np.uint8)
    src1[:, :, 2] = 255
    min_img5_src1 = cv2.min(img5, src1)
    cv2.imshow('min_img5_src1', min_img5_src1)

    cv2.waitKey(0)
    cv2.destroyAllWindows()