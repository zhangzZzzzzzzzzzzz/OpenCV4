# 二维码的定位和解码
import cv2


if __name__ == '__main__':
    img = cv2.imread('qrcode.png', cv2.IMREAD_GRAYSCALE)
    # 二维码检测和识别
    qr_detect = cv2.QRCodeDetector()
    # 对二维码进行检测
    res, points = qr_detect.detect(img)
    if res:
        print('二维码顶点坐标:\n{}'.format(points))
        # 对二维码进行解码
        ret, straight_qrcode = qr_detect.decode(img, points)
        print('二维码中信息：\n{}'.format(ret))
        cv2.namedWindow("Straight QRcode", cv2.WINDOW_NORMAL)
        cv2.imshow('Straight QRcode', straight_qrcode)
    # 定位并解码二维码
    ret1, points1, straight_qrcode1 = qr_detect.detectAndDecode(img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

