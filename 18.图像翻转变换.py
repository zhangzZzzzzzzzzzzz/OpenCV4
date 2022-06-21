import cv2
import sys


if __name__ == '__main__':
    img = cv2.imread('lena.jpeg')
    if img is None:
        print('Failed to read lena.jpg')
        sys.exit()
    # 垂直翻转y轴
    img1 = cv2.flip(img, 1)
    # 水平翻转x轴
    img2 = cv2.flip(img, 0)
    # 绕两条轴旋转
    img3 = cv2.flip(img, -1)
    cv2.imshow('lena', img)
    cv2.imshow('y轴', img1)
    cv2.imshow('x轴', img2)
    cv2.imshow('原点', img3)
    cv2.waitKey(0)
    cv2.destroyAllWindows()