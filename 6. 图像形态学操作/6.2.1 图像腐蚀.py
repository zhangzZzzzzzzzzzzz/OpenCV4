import cv2
import numpy as np
import sys


def generate_random_color():
    return np.random.randint(0, 255, 3)


def fill_color(img1, n, img2):
    h, w = img1.shape
    res = np.zeros((h, w, 3), img1.dtype)
    random_color = {}
    for c in range(1, n):
        random_color[c] = generate_random_color()
    for i in range(h):
        for j in range(w):
            item = img2[i][j]
            if item == 0:
                pass
            else:
                res[i, j, :] = random_color[item]
    return res


def mark(img, n, stat, cent):
    for i in range(1, n):
        cv2.circle(img, (int(cent[i, 0]), int(cent[i, 1])), 2, (0, 255, 0), -1)
        #color = list(map(lambda x: int(x), generate_random_color()))
        color = generate_random_color().tolist()
        cv2.rectangle(img, (stat[i, 0], stat[i, 1]),
                      (stat[i, 0] + stat[i, 2], stat[i, 1] + stat[i, 3]), color)
        cv2.putText(img, str(i), (int(cent[i, 0] + 5), int(cent[i, 1] + 5)), cv2.FONT_HERSHEY_SIMPLEX,
                    0.5, (0, 0, 255), 1)


if __name__ == '__main__':
    image = np.array([[0, 0, 0, 0, 255, 0],
                      [0, 255, 255, 255, 255, 255],
                      [0, 255, 255, 255, 255, 0],
                      [0, 255, 255, 255, 255, 0],
                      [0, 255, 255, 255, 255, 0],
                      [0, 0, 0, 0, 0, 0]], np.uint8)
    # 分别读取黑背景和白背景图片
    black = cv2.imread('LearnCV_black.png', cv2.IMREAD_GRAYSCALE)
    white = cv2.imread('LearnCV_white.png', cv2.IMREAD_GRAYSCALE)
    rice = cv2.imread('rice.png', cv2.IMREAD_GRAYSCALE)
    # 生成结构元
    structure1 = cv2.getStructuringElement(0, (3, 3))
    structure2 = cv2.getStructuringElement(1, (3, 3))
    # 对img1进行腐蚀
    erode_image = cv2.erode(image, structure2)
    # 分别对黑背景图像和白背景图像进行腐蚀
    erode_black1 = cv2.erode(black, structure1)
    erode_black2 = cv2.erode(black, structure2)
    erode_white1 = cv2.erode(white, structure1)
    erode_white2 = cv2.erode(white, structure2)
    # 将图像转化为二值图像
    rice_BW = cv2.threshold(rice, 50, 255, cv2.THRESH_BINARY)
    # 利用矩形进行腐蚀
    erode_riceBW = cv2.erode(rice_BW[1], structure1)
    # 统计连通区域
    count, dst, stats, centroids = cv2.connectedComponentsWithStats(rice_BW[1], ltype=cv2.CV_16U)
    erode_count, erode_dst, erode_stats, erode_centroids = \
        cv2.connectedComponentsWithStats(erode_riceBW, ltype=cv2.CV_16U)
    # 为不同的连通域填色
    erode_rice = rice
    rice = fill_color(rice, count, dst)
    erode_rice = fill_color(erode_rice, erode_count, erode_dst)
    mark(rice, count, stats, centroids)
    mark(erode_rice, erode_count, erode_stats, erode_centroids)
    cv2.namedWindow('image', cv2.WINDOW_NORMAL)
    cv2.namedWindow('image erode', cv2.WINDOW_NORMAL)
    cv2.imshow('image', image)
    cv2.imshow('image erode', erode_image)
    cv2.imshow('black', black)
    cv2.imshow('black1', erode_black1)
    cv2.imshow('black2', erode_black2)
    cv2.imshow('white', white)
    cv2.imshow('white1', erode_white1)
    cv2.imshow('white2', erode_white2)
    cv2.imshow('rice', rice)
    cv2.imshow('erode_rice', erode_rice)
    cv2.waitKey(0)
    cv2.destroyAllWindows()