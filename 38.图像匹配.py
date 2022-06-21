import cv2
import sys


if __name__ == '__main__':
    image = cv2.imread('matchTemplate_2.jpg')
    template = cv2.imread('match_template_2.jpg')
    if image is None or template is None:
        print('Failed to read img')
        sys.exit()
    # 计算模板的宽和高
    cv2.imshow('image', image)
    cv2.imshow('template', template)
    h, w = template.shape[:2]
    # 模板匹配
    result = cv2.matchTemplate(image, template, cv2.TM_CCOEFF)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    # 计算图像左上角和右下角
    left_top = max_loc
    right_bottom = (left_top[0] + w, left_top[1] + h)
    cv2.rectangle(image, left_top, right_bottom, 255, 2)

    cv2.imshow('result', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()