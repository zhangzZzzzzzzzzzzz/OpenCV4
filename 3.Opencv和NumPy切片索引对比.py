import cv2
import sys
import numpy as np
import datetime


if __name__ == '__main__':
    image = cv2.imread('lena.jpeg')
    if image is None:
        print('Failed to read lena.jpg')
        sys.exit()

    # 对比通道分离
    # 使用opencv中split()函数
    begin1 = datetime.datetime.now()
    for i in range(100000):
        b1, g1, r1 = cv2.split(image)
    end1 = datetime.datetime.now()
    print('通道分离（opencv）：{}s'.format((end1 - begin1).total_seconds()))
    # 使用numpy切片
    begin2 = datetime.datetime.now()
    for i in range(100000):
        b2 = image[:, :, 0]
        g2 = image[:, :, 1]
        r2 = image[:, :, 2]
    end2 = datetime.datetime.now()
    print('通道分离（numpy）：{}s'.format((end2 - begin2).total_seconds()))

    # 将BGR图像转化为RGB图像
    # 使用opencv中cv.cvtColor()函数
    begin3 = datetime.datetime.now()
    for i in range(100000):
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    end3 = datetime.datetime.now()
    print('BRG转RGB(opencv):{}s'.format((end3 - begin3).total_seconds()))
    # 使用numpy中切片和索引
    begin4 = datetime.datetime.now()
    for i in range(100000):
        image_rgb = image[:, :, ::-1] 
    end4 = datetime.datetime.now()
    print('BRG转RGB(numpy):{}s'.format((end4 - begin4).total_seconds()))
