import cv2


if __name__ == '__main__':
    image = cv2.imread('approx.png')
    # 提取图像的边缘
    canny = cv2.Canny(image, 80, 160, 3)
    # 膨胀
    kernel = cv2.getStructuringElement(0, (3, 3))
    canny = cv2.dilate(canny, kernel=kernel)
    # 轮廓检测
    contours, _ = cv2.findContours(canny, 0, 2)
    # 创建图中点A
    point = (300, 100)
    # 判断A点与各个轮廓的距离
    for i in range(len(contours)):
        dis = cv2.pointPolygonTest(contours[i], point, measureDist=True)
        if dis < 0:
            pos = '外部'
        elif dis > 0:
            pos = '内部'
        else:
            pos = '边缘上'
        print('像素A与第{}个轮廓的距离为：{}'
              '它位于轮廓{}'.format(i, round(dis, 2), pos))
