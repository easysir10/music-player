from PyQt5 import QtCore, QtGui, QtWidgets
import PyQt5
import pygame
import sys
import qtawesome
import auto_download as ad
import time
import tools


class LyricWindow(QtWidgets.QDialog):
    def __init__(self, path):
        super().__init__()
        tools.lrcDict = {}
        tools.allTimeList = []
        tools.splitLrc(path)
        self.init_ui()

    def init_ui(self):
        self.setFixedSize(700, 100)
        self.lyric_label = QtWidgets.QLabel(self)
        self.lyric_label.setFixedSize(700, 100)
        self.lyric_label.setAlignment(QtCore.Qt.AlignCenter)

        # 设置窗口透明度
        self.setWindowOpacity(0.2)
        # 隐藏边框
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        #  设置窗口背景透明
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setStyleSheet('''
            QLabel{
                background:white;
                border:none;
                color:#A52A2A;
                font-size:20px;
                font-weight:700;
                font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
            }
            QLabel:hover{
                background:black;
            }
        ''')

    def set_lyric(self, currentPos):
        currentPos_ = round(float(currentPos)/1000, 2)
        if tools.lrcDict == {}:
            self.lyric_label.setText('此歌曲暂无歌词！')
        else:
            if currentPos_ in tools.allTimeList:
                self.lyric_label.setText(tools.lrcDict[currentPos_])

    # 解决窗口拖动问题
    def getRestoreInfo(self):
        return self.restorePos, self.restoreSize

    def mousePressEvent(self, QMouseEvent):
        self.isPressed = True
        self.startMovePos = QMouseEvent.globalPos()
        # print(self.startMovePos)

    def mouseMoveEvent(self, QMouseEvent):
        if self.isPressed:
            movePoint = QMouseEvent.globalPos() - self.startMovePos
            widgetPos = self.pos()
            self.startMovePos = QMouseEvent.globalPos()
            self.move(widgetPos.x() + movePoint.x(), widgetPos.y() + movePoint.y())

    def mouseReleaseEvent(self, QMouseEvent):
        self.isPressed = False
