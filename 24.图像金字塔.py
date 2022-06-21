import cv2
import sys


# 构建高斯金字塔
def gauss_img(image):
    # 设置下采样次数
    level = 3
    img = image.copy()
    gauss_imgages = []
    gauss_imgages.append(G0)
    cv2.imshow('Gauss_0', gauss_imgages[0])
    for i in range(level):
        dst = cv2.pyrDown(img)
        gauss_imgages.append(dst)
        cv2.imshow('Gauss_{}'.format(i+1), dst)
        img = dst.copy()
    return gauss_imgages


# 构建拉普拉斯金字塔
def laplian_image(image):
    gauss_imges = gauss_img(image)
    level = len(gauss_imges)
    for i in range(level-1, 0, -1):
        expand = cv2.pyrUp(gauss_imges[i], dstsize=gauss_imges[i-1].shape[:2])
        lpls = cv2.subtract(gauss_imges[i-1], expand)
        cv2.imshow('Laplacian_{}'.format(level-i), lpls)
    # 构建最上面一层,需先进行下采样再进行上采样
    expand = cv2.pyrUp(cv2.pyrDown(gauss_imges[3]), dstsize=gauss_imges[3].shape[:2])
    lpls = cv2.subtract(gauss_imges[3], expand)
    cv2.imshow('Laplacian_{}'.format(0), lpls)


if __name__ == '__main__':
    G0 = cv2.imread('lena.jpeg')
    if G0 is None:
        print('Failed to read lena.jpeg')
        sys.exit()
    laplian_image(G0)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
