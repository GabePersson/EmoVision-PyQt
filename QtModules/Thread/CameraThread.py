# 创建一个线程类用于处理摄像头读取
import cv2
from PyQt5.QtCore import QThread
from PyQt5.QtGui import QImage


class CameraThread(QThread):

    def __init__(self, parent=None):
        super(CameraThread, self).__init__(parent)
        self.cap = None
        self.running = False
        self.img = QImage()

    def run(self):
        self.cap = cv2.VideoCapture(0)  # 打开摄像头
        self.running = True
        while self.running:
            ret, frame = self.cap.read()  # 读取帧
            if ret:
                # 转换为QImage
                height, width, channel = frame.shape
                bytes_per_line = 3 * width
                self.img = QImage(frame.data, width, height, bytes_per_line, QImage.Format_RGB888).rgbSwapped()
            self.msleep(50)

    def stop(self):
        self.running = False
        self.msleep(100)
        if self.cap is not None:
            self.cap.release()