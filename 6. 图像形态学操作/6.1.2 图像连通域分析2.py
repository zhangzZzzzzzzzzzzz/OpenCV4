# cv2.connectedComponentsWithStats具有不同连通域的统计信息矩阵、质心坐标、面积等参数
import cv2
import numpy as np
import sys


def generate_random_color():
    return np.random.randint(0, 255, 3)


def fill_color(img1, n, img2):
    h, w = img1.shape[:2]
    res = np.zeros((h, w, 3), dtype=img1.dtype)
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


def mask(img, n, stat, cent):
    for i in range(1, n):
        # 绘制中心点
        cv2.circle(img, (int(cent[i, 0]), int(cent[i, 1])), 2, (0, 255, 0))
        # 绘制连通域矩形外框
        color = list(map(lambda x: int(x), generate_random_color()))
        print(color)
        cv2.rectangle(img, (stat[i, 0], stat[i, 1]), (stat[i, 0] + stat[i, 2], stat[i, 1] + stat[i, 3]), color)
        # 标记数字
        cv2.putText(img, str(i), (int(cent[i, 0]), int(cent[i, 1])), cv2.FONT_HERSHEY_SIMPLEX,
                    fontScale=0.5, color=(0, 0, 255))


if __name__ == '__main__':
    rice = cv2.imread('rice.png', cv2.IMREAD_GRAYSCALE)
    rice_BW = cv2.threshold(rice, 50, 255, cv2.THRESH_BINARY)
    # 统计连通域信息
    count, dst, states, centroids = cv2.connectedComponentsWithStats(rice_BW[1], ltype=cv2.CV_16U)
    # 为不同的连通域填色
    result = fill_color(rice, count, dst)
    # 绘制外接矩形及矩形中心点，并进行标记
    mask(result, count, states, centroids)
    # 输出每个连通区域的面积
    for s in range(1, count):
        print('第{}个连通域的面积为：{}'.format(s, states[s, 4]))
    cv2.imshow('Origin', rice)
    cv2.imshow('result', result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()