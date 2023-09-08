import cv2

if __name__ == '__main__':

    cap = cv2.VideoCapture('http://192.168.1.1:8080/?action=stream')  # 读取视频
    print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    while cap.isOpened():  # 当视频被打开时：
        ret, frame = cap.read()  # 读取视频，读取到的某一帧存储到frame，若是读取成功，ret为True，反之为False
        if ret:  # 若是读取成功
            cv2.imshow('frame', frame)  # 显示读取到的这一帧画面
            key = cv2.waitKey(25)  # 等待一段时间，并且检测键盘输入
            if key == ord('q'):  # 若是键盘输入'q',则退出，释放视频
                cap.release()  # 释放视频
                break
        else:
            cap.release()
    cv2.destroyAllWindows()  # 关闭所有窗口

