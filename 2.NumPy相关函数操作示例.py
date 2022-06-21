import cv2
import numpy as np
import datetime
import sys


if __name__ == '__main__':
    # 创建 ndarry 对象
    # 使用np.array（）创建一个5*5、数据类型为folat32的矩阵
    a = np.array([[1, 2, 3, 4, 5],
                  [6, 7, 8, 9, 10],
                  [11, 12, 13, 14, 15],
                  [16, 17, 18, 19, 20],
                  [21, 22, 23, 24, 25]], dtype='float32')
    # 使用np.ones
    b = np.ones((5, 5), dtype='uint8')
    # 使用np.zeros
    c = np.zeros((5, 5), dtype='float32')
    d = 1
    print('创建对边np.array:\n{}'.format(a))
    print('创建对边np.ones:\n{}'.format(b))
    print('创建对边np.zeros:\n{}'.format(c))

    # ndarray对象的切片和索引
    image = cv2.imread('lena.jpeg')
    if image is None:
        print('Failed to read lena.jpeg')
        sys.exit()
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # 读取图像位于(45, 45)的图像
    print('图像位于（45，45）的像素值为{}'.format(image[45, 45]))

    # 裁剪部分图像
    res_gray = gray[40:280, 60:340]
    res_color1 = image[40:280, 60:340]
    res_color2 = image[100:220, 80:220]

    # 通道分离
    b = image[:, :, 0]
    g = image[:, :, 1]
    r = image[:, :, 2]
    b1, g1, r1 = cv2.split(image)
    # 展示裁剪和分离通道的结果
    cv2.imshow('Result crop gray', res_gray)
    cv2.imshow('Result crop color1', res_color1)
    cv2.imshow('Result crop color2', res_color2)
    cv2.imshow('Result split b', b)
    cv2.imshow('Result split g', g)
    cv2.imshow('Result split r', r)
    cv2.imshow('Result split b1', b1)
    cv2.imshow('Result split g1', g1)
    cv2.imshow('Result split r1', r1)

    # 生成随机数
    # 生成一个5*5、取值范围为0-100的数组
    value1 = np.random.randint(0, 100, (5, 5), dtype='uint8')
    # 生成一个2*3、元素服从均值0、标准差1为正态分布的数组
    value2 = np.random.randn(2, 3)
    print('生成的随机数 np.random.randint：\n{}'.format(value1))
    print('生成的随机数 np.random.randn：\n{}'.format(value2))

    cv2.waitKey(0)
    cv2.destroyAllWindows()


