import cv2


if __name__ == '__main__':
    video = cv2.VideoCapture('road.mp4')
while video.isOpened():
    ret, img = video.read()
    if ret:
        cv2.imshow('video', img)
        cv2.waitKey(int(1000/video.get(cv2.CAP_PROP_FPS)))
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
# 输出相关视频信息
print('视频中图像的宽度为{}'.format(video.get(cv2.CAP_PROP_FRAME_WIDTH)))
print('视频中图像的高度为{}'.format(video.get(cv2.CAP_PROP_FRAME_HEIGHT)))
print('视频中的帧率为{}'.format(video.get(cv2.CAP_PROP_FPS)))
print('视频的总帧数为{}'.format(video.get(cv2.CAP_PROP_FRAME_COUNT)))
# 释放关闭窗口
video.release()
cv2.destroyAllWindows()
