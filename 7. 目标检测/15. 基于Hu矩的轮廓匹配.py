import cv2


if __name__ == '__main__':
    image1 = cv2.imread('ABC.png')
    image2 = cv2.imread('B.png')
    # 灰度化
    gray1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)
    # 二值化
    _, binary1 = cv2.threshold(gray1, 0, 255, cv2.THRESH_BINARY)
    _, binary2 = cv2.threshold(gray2, 0, 255, cv2.THRESH_BINARY)
    # 轮廓检测
    contours1, _ = cv2.findContours(binary1, mode=cv2.RETR_TREE, method=cv2.CHAIN_APPROX_SIMPLE)
    contours2, _ = cv2.findContours(binary2, mode=cv2.RETR_TREE, method=cv2.CHAIN_APPROX_SIMPLE)
    # Hu矩计算
    hu = cv2.HuMoments(cv2.moments(contours2[0]))
    # 轮廓检测
    for i in range(len(contours1)):
        hu1 = cv2.HuMoments(cv2.moments(contours1[i]))
        dist = cv2.matchShapes(hu1, hu, cv2.CONTOURS_MATCH_I1, 0)
        if dist < 1:
            cv2.drawContours(image1, contours1, i, (0, 0, 255), 3, 8)
    cv2.imshow('Match Result', image1)
    cv2.waitKey(0)
    cv2.destroyAllWindows()