import cv2
import sys


if __name__ == '__main__':
    img = cv2.imread('Gray_dolphins.jpg')
    img_gauss = cv2.imread('GrayGaussImage.jpg')
    img_salt = cv2.imread('GraySaltPepperImage.jpg')

    result1_5 = cv2.GaussianBlur(img, (5, 5), 10, 20)
    result1_9 = cv2.GaussianBlur(img, (9, 9), 10, 20)
    result_5_gauss = cv2.GaussianBlur(img_gauss, (5, 5), 10, 20)
    result_9_gauss = cv2.GaussianBlur(img_gauss, (9, 9), 10, 20)
    result_5_salt = cv2.GaussianBlur(img_salt, (5, 5), 10, 20)
    result_9_salt = cv2.GaussianBlur(img_salt, (9, 9), 10, sigmaY=20)

    cv2.imshow('Origin Image', img)
    cv2.imshow('result1_5', result1_5)
    cv2.imshow('result1_9', result1_9)
    cv2.imshow('img_gauss', img_gauss)
    cv2.imshow('result_5_gauss', result_5_gauss)
    cv2.imshow('result_9_gauss', result_9_gauss)
    cv2.imshow('img_salt', img_salt)
    cv2.imshow('result_5_salt', result_5_salt)
    cv2.imshow('result_9_salt', result_9_salt)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

