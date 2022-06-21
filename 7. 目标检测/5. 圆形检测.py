import cv2
import sys


def draw_circle(img, values):
    for i in values[0, :]:
        cv2.circle(img, (int(i[0]), int(i[1])), int(i[2]), (255, 0, 0), 2)
        cv2.circle(img, (int(i[0]), int(i[1])), 2, (0, 255, 0), 3)


if __name__ == '__main__':
    image = cv2.imread('circles.png')
    if image is None:
        print('Failed to read image')
        sys.exit()

    cv2.imshow('Origin', image)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # 高斯滤波
    gray = cv2.GaussianBlur(gray, (9, 9), sigmaX=2, sigmaY=2)
    # 设置参数
    dp = 1.5
    min_dist = 20
    param1 = 100
    param2 = 100
    min_radius = 20
    max_radius = 100
    # 检测圆形
    circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, dp, min_dist, param1=param1, param2=param2, minRadius=
                             min_radius, maxRadius=max_radius)
    # 绘制圆形
    draw_circle(image, circles)

    cv2.imshow('Detect Circle Result', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
