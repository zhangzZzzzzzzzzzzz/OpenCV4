import cv2
import sys


def my_bur(image):
    return cv2.blur(image, (3, 3)), cv2.blur(image, (7, 7))


if __name__ == '__main__':
    img = cv2.imread('Gray_dolphins.jpg')
    img_salt = cv2.imread('GraySaltPepperImage.jpg')
    img_gauss = cv2.imread('GrayGaussImage.jpg')
    if img is None or img_salt is None or img_gauss is None:
        print('Failed to read img')
        sys.exit()
    img1, img2 = my_bur(img)
    img_salt1, img_salt2 = my_bur(img_salt)
    img_gauss1, img_gauss2 = my_bur(img_gauss)
    cv2.imshow('Origin Image', img)
    cv2.imshow('3*3 blur image', img1)
    cv2.imshow('7*7 blur image', img2)
    cv2.imshow('Img_salt', img_salt)
    cv2.imshow('3*3 salt_blur image', img_salt1)
    cv2.imshow('7*7 salt_blur image', img_salt2)
    cv2.imshow('Img_gauss', img_gauss)
    cv2.imshow('3*3 gauss_blur image', img_gauss1)
    cv2.imshow('7*7 gauss_blur image', img_gauss2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()