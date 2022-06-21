import cv2
import sys


if __name__ == '__main__':
    img1 = cv2.imread('lena.jpeg')
    if img1 is None:
        print('Fail to open lena.jpg')
        sys.exit()
    else:
        print('图像的形状：{}\n元素的数据类型：{}\n图像的通道数：{}\n像素总数：{}'
              .format(img1.shape, img1.dtype, img1.ndim, img1.size))

