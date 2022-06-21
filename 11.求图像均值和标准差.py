import cv2
import numpy as np


if __name__ == '__main__':
    # 新建array
    img = np.array([1, 2, 3, 4, 5, 10, 6, 7, 8, 9, 10, 0])
    # 将array调整为3*4的单通道图像
    img1 = img.reshape((3, 4))
    # 将array调整为3*2*2的多通道图像
    img2 = img.reshape((3, 2, 2))

    mean_img1 = cv2.mean(img1)
    mean_img2 = cv2.mean(img2)
    mean_std1, mean_std_dev_img1 = cv2.meanStdDev(img1)
    mean_std2, mean_std_dev_img2 = cv2.meanStdDev(img2)

    print('cv.mean()计算的结果如下：')
    print('图像img1的均值为：{}'.format(mean_img1))
    print('图像img2的均值为：{},\n其中第1个通道的均值为{}\n,第2个通道的均值为{}'.format(mean_img2, mean_img2[0], mean_img2[1]))
    print('cv.meanStdDev计算的结果如下：')
    print('图像img1的均值为：{},\n标准差为{}'.format(mean_std1[0], mean_std_dev_img1[0]))
    print('图像img2的均值为：{},\n其中第1个通道的均值为{}\n,第2个通道的均值为{}\n'
          '图像img2的标准差为：{},\n其中第1个通道的标准差为{}\n,第2个通道的标准差为{}\n'.format(mean_std2, mean_std2[0],
                                mean_std2[1], mean_std_dev_img2, mean_std_dev_img2[0], mean_std_dev_img2[1]))
