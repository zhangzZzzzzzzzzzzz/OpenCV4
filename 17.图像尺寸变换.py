import cv2
import sys
# 图像缩小插值运用cv2.INTER_AREA
# 图像放大插值运用cv2.INTER_LINEAR 或cv2.INTER_CUBIC


if __name__ == '__main__':
    # 读取图像并判断是否读取成功
    img = cv2.imread('lena.jpeg', cv2.IMREAD_GRAYSCALE)
    if img is None:
        print('Failed to read lena.jpg')
        sys.exit()
    small_img1 = cv2.resize(img, (15, 15), fx=0, fy=0, interpolation=cv2.INTER_AREA)
    big_img1 = cv2.resize(small_img1, (30, 30), fx=0, fy=0, interpolation=cv2.INTER_NEAREST)
    big_img2 = cv2.resize(small_img1, (30, 30), fx=0, fy=0, interpolation=cv2.INTER_LINEAR)
    big_img3 = cv2.resize(small_img1, (30, 30), fx=0, fy=0, interpolation=cv2.INTER_CUBIC)
    cv2.namedWindow('small', cv2.WINDOW_NORMAL)
    cv2.imshow('small', small_img1)
    cv2.namedWindow('big_img1', cv2.WINDOW_NORMAL)
    cv2.imshow('big_img1', big_img1)
    cv2.namedWindow('big_img2', cv2.WINDOW_NORMAL)
    cv2.imshow('big_img2', big_img2)
    cv2.namedWindow('big_img3', cv2.WINDOW_NORMAL)
    cv2.imshow('big_img3', big_img3)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
