import sys
import os
import cv2

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *

from ui.main_ui import Ui_main
from PyQt5.QtCore import Qt

from car_control.car_control import *

import time

import subprocess
import threading


class Ui_MainWindow(QtWidgets.QWidget, Ui_main):

    def __init__(self, url):
        super(Ui_MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("基于肌电信号的残疾人智能辅助系统")
        self.setWindowFlags(Qt.WindowCloseButtonHint)

        self._lock = _lock = threading.Lock()

        self.timer_camera = QtCore.QTimer()  # 初始化定时器
        self.url = url
        self.cap = None

        self.timer_emg = QtCore.QTimer()

        self.is_robot_grab = False
        self.is_robot_forward = False

        self.mode = 0

        self.motion = []
        self.is_motion_update = False
        self.last_motion_time = None

        self.cameraButton.clicked.connect(self.button_open_camera_click)
        self.timer_camera.timeout.connect(self.show_camera)
        self.timer_emg.timeout.connect(self.collect_emg_result)
        self.grabButton.clicked.connect(self.grab_object)
        self.leftButton.clicked.connect(self.robot_left)
        self.rightButton.clicked.connect(self.robot_right)
        self.forwardButton.clicked.connect(self.robot_forward)
        self.resetButton.clicked.connect(self.stop_robot)
        self.emgButton.clicked.connect(self.click_start_emg)
        self.comboBox.currentIndexChanged.connect(self.change_mode)

        motion_visible = False

        self.grabButton.setVisible(motion_visible)
        self.leftButton.setVisible(motion_visible)
        self.rightButton.setVisible(motion_visible)
        self.forwardButton.setVisible(motion_visible)

        reset()

        threading.Thread(target=Ui_MainWindow.start_emg, args=(self,)).start()

    def change_mode(self):
        index = self.comboBox.currentIndex()
        # print(f'change:{index}')
        self.mode = index
        if self.timer_emg.isActive():
            self.click_start_emg()
        self.textBrowser.append(f'>>>>>   切换模式: {self.comboBox.currentText()}')
        self.textBrowser.ensureCursorVisible()

    def collect_emg_result(self):
        is_end = False
        action_list = ['forward', 'right', 'left', 'none']
        action_dict = {'forward': 0, 'left': 0, 'right': 0}
        with self._lock:
            # print(f'motion length:{len(self.motion)}')
            print(f'motion:{self.motion}')
            s_motion = None
            for x in self.motion:
                if x not in action_list:
                    print(f'illegal action: {x}')
                    self.motion.clear()
                    return
                if x == 'none':
                    if is_end:
                        break
                    else:
                        continue
                else:
                    s_motion = x
                    action_dict[x] += 1
            self.motion.clear()
        if action_dict['forward'] == 0 and action_dict['left'] == 0 and action_dict['right'] == 0:
            return

        print(action_dict)
        motion = max(action_dict, key=action_dict.get)

        # small trick
        if action_dict['right'] >= 2:
            motion = 'right'

        if s_motion == 'forward':
            motion = 'forward'

        this_time = time.time()
        if self.last_motion_time is not None and this_time - self.last_motion_time < 3:
            return
        self.last_motion_time = this_time

        # print(f'motion:{motion}')
        if self.mode == 1:
            if motion == 'forward':
                if self.is_robot_forward:
                    action = '停止'
                    self.set_browser_action(motion, action, this_time)
                    self.update()
                    stop()
                else:
                    action = '前进'
                    self.set_browser_action(motion, action, this_time)
                    self.update()
                    forward()
                self.is_robot_forward = not self.is_robot_forward
            elif motion == 'left':
                action = '左转'
                self.set_browser_action(motion, action, this_time)
                self.update()
                left()
                self.is_robot_forward = False
            elif motion == 'right':
                action = '右转'
                self.set_browser_action(motion, action, this_time)
                self.update()
                right()
                self.is_robot_forward = False
            # elif motion == 'grab':
            #     if self.is_robot_grab:
            #         action = '松开'
            #         self.set_browser_action(motion, action)
            #         loosen()
            #     else:
            #         action = '抓取'
            #         self.set_browser_action(motion, action)
            #
            #         grab()
            else:
                return
        elif self.mode == 0:
            if motion == 'forward':
                action = '路线1: 取水杯'
                self.set_browser_action(motion, action, this_time)
                self.update()
                # print('2')
                get_object_2()
            elif motion == 'left':
                action = '路线2: 放置物品'
                self.set_browser_action(motion, action, this_time)
                self.update()
                get_object_1()
            elif motion == 'right':
                action = '路线3: 喂猫'
                self.set_browser_action(motion, action, this_time)
                self.update()
                get_object_3()
            else:
                return
        else:
            return

        self.motion.clear()

    def set_browser_action(self, motion, action, action_time):
        self.textBrowser.append(
            f'[{time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(action_time))}] 信号: {motion}, 动作: {action}')
        self.textBrowser.ensureCursorVisible()
        # self.textBrowser.update()
        QApplication.processEvents()

    def robot_forward(self):
        if self.is_robot_forward:
            stop()
            self.forwardButton.setText('前进')
        else:
            forward()
            self.forwardButton.setText('停止')
        self.is_robot_forward = not self.is_robot_forward

    def robot_left(self):
        left()

    def robot_right(self):
        right()

    def stop_robot(self):
        stop()
        self.is_robot_forward = False
        QMessageBox.information(self, "强制停止", "小车强制停止成功")

    def grab_object(self):
        if not self.is_robot_grab:
            grab()
            self.grabButton.setText('放下')
        else:
            loosen()
            self.grabButton.setText('抓取')

        self.is_robot_grab = not self.is_robot_grab

    def button_open_camera_click(self):
        if not self.timer_camera.isActive():
            try:
                self.cap = cv2.VideoCapture(self.url)
            except Exception:
                QMessageBox.information(self, "摄像头连接失败", "请检查小车及摄像头连接性",
                                        QMessageBox.Yes)
                return
            self.timer_camera.start(2)
            self.cameraButton.setText(u'关闭摄像头')
        else:
            self.timer_camera.stop()
            self.cap.release()
            self.video.clear()
            self.video.setText('无视频信号')
            self.cameraButton.setText(u'打开摄像头')

    def click_start_emg(self):
        # threading.Thread(target=Ui_MainWindow.start_emg, args=(self,)).start()
        if self.timer_emg.isActive():
            self.timer_emg.stop()
            # self.textBrowser.setText('')
            self.emgButton.setText('开启肌电采集')
        else:
            self.timer_emg.start(1000)
            with self._lock:
                self.motion.clear()
            # threading.Thread(target=simulate).start()
            self.emgButton.setText('关闭肌电采集')

    def start_emg(self):
        proc_data = subprocess.Popen(
            "D:\\Python\\Anaconda\\envs\\Torch\\python.exe get_input_data.py",
            cwd='.',
            stdin=subprocess.DEVNULL,
            stdout=subprocess.PIPE,
            # stderr=subprocess.PIPE
        )
        proc_algo = subprocess.Popen(
            "D:\\Python\\Anaconda\\envs\\Torch\\python.exe predict.py",
            cwd='.',
            stdin=proc_data.stdout,
            stdout=subprocess.PIPE,

        )
        assert proc_algo.stdout
        # print(proc_data.stderr)
        # for line in proc_data.stdout:
        #     print(line.decode())

        for line in proc_algo.stdout:
            with self._lock:
                self.motion.append(line.decode().strip())
                # self.is_motion_update = True
        while proc_data.poll() is None or proc_algo.poll() is None:
            continue

    def show_camera(self):
        flag, image = self.cap.read()
        if flag:
            show = cv2.resize(image, (720, 440))
            show = cv2.cvtColor(show, cv2.COLOR_BGR2RGB)
            show_image = QtGui.QImage(show.data, show.shape[1], show.shape[0], QtGui.QImage.Format_RGB888)
            self.video.setPixmap(QtGui.QPixmap.fromImage(show_image))

    def closeEvent(self, event):
        ok = QtWidgets.QPushButton()
        cancel = QtWidgets.QPushButton()
        msg = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Warning, u'关闭', u'是否关闭！')
        msg.addButton(ok, QtWidgets.QMessageBox.ActionRole)
        msg.addButton(cancel, QtWidgets.QMessageBox.RejectRole)
        ok.setText(u'确定')
        cancel.setText(u'取消')

        if msg.exec_() == QtWidgets.QMessageBox.RejectRole:
            event.ignore()
        else:
            self.timer_emg.stop()

            if self.cap is not None and self.cap.isOpened():
                self.cap.release()
            if self.timer_camera.isActive():
                self.timer_camera.stop()
            event.accept()


if __name__ == '__main__':
    robot_url = 'http://192.168.1.1:8080/?action=stream'

    App = QApplication(sys.argv)
    win = Ui_MainWindow(robot_url)
    win.show()
    sys.exit(App.exec_())
