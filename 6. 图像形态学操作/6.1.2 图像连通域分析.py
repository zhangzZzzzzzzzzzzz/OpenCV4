# cv2.connectedComponents 通过标签将不同的连通域区分开
import cv2
import numpy as np
import sys


def generate_random_color():
    return np.random.randint(0, 256, 3)


def fill_color(img1, img2):
    h, w = img1.shape
    res = np.zeros((h, w, 3), img1.dtype)
    # 生成随机颜色
    random_color = {}
    for c in range(1, count):
        random_color[c] = generate_random_color()
    # 为不同的连通域填色
    for i in range(h):
        for j in range(w):
            item = img2[i][j]
            if item == 0:
                pass
            else:
                res[i, j, :] = random_color[item]
    return res


if __name__ == '__main__':
    rice = cv2.imread('rice.png', cv2.IMREAD_GRAYSCALE)
    # 转化为二值图像
    rice_BW = cv2.threshold(rice, 50, 255, cv2.THRESH_BINARY)
    # 统计连通域
    count, res = cv2.connectedComponents(rice_BW[1], ltype=cv2.CV_16U)
    # 以不同的颜色标记出不同的连通域
    result = fill_color(rice_BW[1], res)
    print(count)
    cv2.imshow('Origin', rice)
    cv2.imshow('Result', result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


