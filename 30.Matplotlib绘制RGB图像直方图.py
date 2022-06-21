import cv2
import sys
from matplotlib import pyplot as plt


if __name__ == '__main__':
    img = cv2.imread('flower.jpg')
    if img is None:
        print('Failed to read img')
        sys.exit()
    color = ('b', 'g', 'r')
    for i, col in enumerate(color):
        hist_item = cv2.calcHist([img], [i], None, [256], [0, 256])
        print(hist_item.shape)
        plt.plot(hist_item, color=col)
    cv2.imshow('img', img)
    plt.show()
    cv2.waitKey(0)
    cv2.destroyAllWindows()

