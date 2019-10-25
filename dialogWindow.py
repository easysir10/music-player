from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import qtawesome
import auto_download as ad
import time


class DialogWindow(QtWidgets.QDialog):
    def __init__(self, dic, auto_download):
        super().__init__()
        self.init_ui()
        self.dic = dic
        self.auto_download = auto_download
        self.music_show(dic)
        self.exec_()

    def init_ui(self):
        self.setWindowTitle('搜索结果(双击下载歌曲)')
        self.setFixedSize(510, 280)
        # 隐藏边框
        # self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        # 创建列表控件
        self.results_list = QtWidgets.QListWidget(self)
        # 隐藏横竖滚动条
        self.results_list.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.results_list.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.results_list.doubleClicked.connect(lambda: self.music_download(self.results_list))

        self.results_list.setFixedSize(510, 280)
        # 美化界面
        self.setStyleSheet('''
            QListWidget{
                border:none;
                color:gray;
                font-size:13px;
                height:45px;
                text-align:left;
                padding:10px;
            }
            QListWidget::item:hover{
                color:black;
                border:1px solid #F3F3F5;
                border-radius:10px;
                background:LightGray;
            }
            QDialog{
                background:white;
                border-top-right-radius:10px;
                border-bottom-right-radius:10px;
                border-top-left-radius:10px;
                border-bottom-left-radius:10px;
            }
        ''')

    def music_show(self, dic):
        for key, v in dic.items():
            # 把字符串转化为QListWidgetItem项目对象
            item = QtWidgets.QListWidgetItem(v)
            # 添加项目
            self.results_list.addItem(item)

    # 下载音乐
    def music_download(self, results_list):
        for k, v in self.dic.items():
            if v == results_list.currentItem().text():
                key = k
        self.auto_download.download(key, results_list.currentItem().text())
