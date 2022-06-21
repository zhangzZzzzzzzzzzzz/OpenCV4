import cv2
import sys


if __name__ == '__main__':
    img = cv2.imread('ColorSaltPepperImage.jpg')
    gray = cv2.imread('GraySaltPepperImage.jpg')
    if img is None or gray is None:
        print('Failed to read img')
        sys.exit()
    img_3 = cv2.medianBlur(img, 3)
    img_9 = cv2.medianBlur(img, 9)
    gray_3 = cv2.medianBlur(gray, 3)
    gray_9 = cv2.medianBlur(gray, 9)

    cv2.imshow('Origin SaltImage', img)
    cv2.imshow('img 3*3', img_3)
    cv2.imshow('img 9*9', img_9)
    cv2.imshow('Origin GraySalt', gray)
    cv2.imshow('gray 3*3', gray_3)
    cv2.imshow('gray 9*9', gray_9)

    cv2.waitKey(0)
    cv2.destroyAllWindows()