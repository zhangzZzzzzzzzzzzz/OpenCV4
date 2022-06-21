import cv2
import sys
import numpy as np


bins = np.arange(256).reshape(256, 1)


def draw_gray_histogram(image):
    # 创建一个全0矩阵以绘制直方图
    new = np.zeros((image.shape[0], 256, 3))
    # 对图像进行直方图计算
    hist_item = cv2.calcHist([image], [0], None, [256], [0, 256])
    # 对直方图进行归一化
    cv2.normalize(hist_item, hist_item, 0, 255, cv2.NORM_MINMAX)
    hist = np.int32(np.around(hist_item, decimals=0))
    hist = hist.flatten()
    for x, y in enumerate(hist):
        cv2.line(new, (x, 0), (x, y), (255, 255, 255))
    result = cv2.flip(new, 0)
    return result


def draw_bgr_histogram(image):
    # 创建一个3通道全为0矩阵以绘制直方图
    new = np.zeros((image.shape[0], 256, 3))
    bgr = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]
    for i, col in enumerate(bgr):
        hist_item = cv2.calcHist([image], [i], None, [256], [0, 256])
        cv2.normalize(hist_item, hist_item, 0, 255, cv2.NORM_MINMAX)
        hist = np.int32(np.around(hist_item))
        hist = np.int32(np.column_stack((bins, hist)))
        print(hist.shape)
        cv2.polylines(new, [hist], True, col)
    result = cv2.flip(new, 0)
    return result


if __name__ == '__main__':
    img = cv2.imread('flower.jpg')
    if img is None:
        print('Failed to read img')
        sys.exit()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    # 计算并绘制灰度图像的直方图和BGR图像的直方图
    gray_histogram = draw_gray_histogram(gray)
    bgr_histogram = draw_bgr_histogram(img)
    cv2.imshow('Origin Image', img)
    cv2.imshow('Gray Histogram', gray_histogram)
    cv2.imshow('BGR Histogram', bgr_histogram)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


