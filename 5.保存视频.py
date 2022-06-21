import cv2


if __name__ == '__main__':
    # 设置编解码方式
    fource = cv2.VideoWriter_fourcc(*'DIVX')
    video = cv2.VideoCapture('road.mp4')
    result = cv2.VideoWriter('Save.avi', fource, 1, (640, 368))

    while video.isOpened():
        ret, frame = video.read()
        if ret is True:
            frame = cv2.flip(frame, 1)
            cv2.imshow('video', frame)
            result.write(frame)
            cv2.waitKey(5)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break
    video.release()
    result.release()
    cv2.destroyAllWindows()