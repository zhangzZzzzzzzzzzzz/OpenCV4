import cv2
import sys
from matplotlib import pyplot as plt


if __name__ == '__main__':
    img = cv2.imread('flower.jpg', 0)
    if img is None:
        print('Failed to rean img.jpg')
        sys.exit()
    print(img)
    print(img.ravel().shape)
    # 绘制直方图
    _, _, _ = plt.hist(img.ravel(), bins=256, range=[0, 256])
    cv2.imshow('image', img)
    plt.show()
    cv2.waitKey(0)
    cv2.destroyAllWindows()