# coding:utf-8

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import qtawesome
import utils
import dialogWindow
import lyricWindow
import auto_download as ad
import pygame
import time
from mutagen.mp3 import MP3
from threading import Thread
import tools
import signal
import inspect
import ctypes
import random


class MainUi(QtWidgets.QMainWindow):
    pygame.mixer.init()

    def __init__(self):
        super().__init__()
        self.setFixedSize(1020, 570)
        # 创建窗口主部件
        self.main_widget = QtWidgets.QWidget()
        # 创建主部件的网格布局
        self.main_layout = QtWidgets.QGridLayout()
        # 设置窗口主部件布局为网格布局
        self.main_widget.setLayout(self.main_layout)
        # 设置窗口主部件
        self.setCentralWidget(self.main_widget)
        # 初始化左侧ui
        self.init_left_ui()
        # 初始化右侧ui
        self.init_right_ui()
        # 设置窗口透明度
        self.setWindowOpacity(1)
        # 设置窗口背景透明
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        # 隐藏边框
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.main_layout.setSpacing(0)
        self.main_widget.setStyleSheet('''
            QWidget#left_widget{
                background:#F7F7F7;
                border-top:1px solid white;
                border-bottom:1px solid white;
                border-left:1px solid white;
                border-top-left-radius:10px;
                border-bottom-left-radius:10px;
            }
        ''')

        self.right_close.clicked.connect(self.close)
        self.t = Thread()
        self.lyric_t = Thread()

    def init_left_ui(self):
        # 创建左侧菜单栏
        self.left_widget = QtWidgets.QWidget()
        self.left_widget.setObjectName('left_widget')
        # 创建左侧部件的网格布局层
        self.left_layout = QtWidgets.QGridLayout()
        # 设置左侧部件布局为网格
        self.left_widget.setLayout(self.left_layout)
        # 左侧部件在第0行第0列，占12行2列
        self.main_layout.addWidget(self.left_widget, 0, 0, 12, 1)

        self.flag = QtWidgets.QToolButton()
        # 设置按钮文本
        self.flag.setText("心随乐动")
        # 设置按钮图标
        self.flag.setIcon(QtGui.QIcon('images/myMusic.png'))
        # 设置图标大小
        self.flag.setIconSize(QtCore.QSize(50, 50))
        # 设置按钮形式为上图下文
        self.flag.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)

        self.left_label_1 = QtWidgets.QPushButton("每日推荐")
        self.left_label_1.setObjectName('left_label')
        self.left_label_2 = QtWidgets.QPushButton("我的音乐")
        self.left_label_2.setObjectName('left_label')
        self.left_label_3 = QtWidgets.QPushButton("联系与帮助")
        self.left_label_3.setObjectName('left_label')

        self.left_button_1 = QtWidgets.QPushButton(qtawesome.icon('fa.music', color='gray'), "华语流行")
        self.left_button_1.setObjectName('left_button')
        self.left_button_2 = QtWidgets.QPushButton(qtawesome.icon('fa.sellsy', color='gray'), "在线FM")
        self.left_button_2.setObjectName('left_button')
        self.left_button_3 = QtWidgets.QPushButton(qtawesome.icon('fa.film', color='gray'), "热门MV")
        self.left_button_3.setObjectName('left_button')
        self.left_button_4 = QtWidgets.QPushButton(qtawesome.icon('fa.home', color='gray'), "本地音乐")
        self.left_button_4.setObjectName('left_button')
        self.left_button_5 = QtWidgets.QPushButton(qtawesome.icon('fa.download', color='gray'), "下载管理")
        self.left_button_5.setObjectName('left_button')
        self.left_button_6 = QtWidgets.QPushButton(qtawesome.icon('fa.heart', color='gray'), "我的收藏")
        self.left_button_6.setObjectName('left_button')
        self.left_button_7 = QtWidgets.QPushButton(qtawesome.icon('fa.comment', color='gray'), "反馈建议")
        self.left_button_7.setObjectName('left_button')
        self.left_button_8 = QtWidgets.QPushButton(qtawesome.icon('fa.star', color='gray'), "关注我们")
        self.left_button_8.setObjectName('left_button')
        self.left_button_9 = QtWidgets.QPushButton(qtawesome.icon('fa.question', color='gray'), "遇到问题")
        self.left_button_9.setObjectName('left_button')
        self.left_xxx = QtWidgets.QPushButton(" ")

        self.left_layout.addWidget(self.flag, 0, 0, 1, 3)
        self.left_layout.addWidget(self.left_label_1, 1, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_1, 2, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_2, 3, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_3, 4, 0, 1, 3)
        self.left_layout.addWidget(self.left_label_2, 5, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_4, 6, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_5, 7, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_6, 8, 0, 1, 3)
        self.left_layout.addWidget(self.left_label_3, 9, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_7, 10, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_8, 11, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_9, 12, 0, 1, 3)

        # 设置左侧按钮样式
        self.left_widget.setStyleSheet('''
            QPushButton{border:none;color:gray;}
            QPushButton#left_label{
                border:none;
                border-bottom:1px solid white;
                font-size:18px;
                font-weight:700;
                font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
            }
            QPushButton#left_button:hover{border-left:4px solid red;font-weight:700;}
            QToolButton{
                border:none;
                font-size:20px;
                font-weight:700;
                font-family: Helvetica, Arial, sans-serif;}
        ''')

    def init_right_ui(self):
        # 创建右侧部件
        self.right_widget = QtWidgets.QWidget()
        # 创建右侧部件的网格布局层
        self.right_widget.setObjectName('right_widget')
        self.right_layout = QtWidgets.QGridLayout()
        # 设置右侧部件布局为网格
        self.right_widget.setLayout(self.right_layout)
        # 右侧部件在第0行第2列，占12行10列
        self.main_layout.addWidget(self.right_widget, 0, 1, 12, 11)

        # 右侧顶部搜索框部件
        self.right_bar_widget = QtWidgets.QWidget()
        # 右侧顶部搜索框网格布局
        self.right_bar_layout = QtWidgets.QGridLayout()
        self.right_bar_widget.setLayout(self.right_bar_layout)
        self.search_icon = QtWidgets.QLabel(chr(0xf002) + '' + '搜索')
        self.search_icon.setFont(qtawesome.font('fa', 15))
        self.right_bar_widget_search_input = QtWidgets.QLineEdit()
        self.right_bar_widget_search_input.setPlaceholderText("输入歌手或歌曲，回车进行搜索")
        self.right_bar_widget_search_input.grabKeyboard()

        self.right_bar_layout.addWidget(self.search_icon, 0, 0, 1, 1)
        self.right_bar_layout.addWidget(self.right_bar_widget_search_input, 0, 1, 1, 6)
        self.right_layout.addWidget(self.right_bar_widget, 0, 0, 1, 6)

        # 设置搜索框样式
        self.right_bar_widget_search_input.setStyleSheet(
            '''QLineEdit{
                    border:1px solid gray;
                    width:100px;
                    height:25px;
                    border-radius:5px;
                    padding:1px 2px;
            }''')
        # 设置右侧圆角
        self.right_widget.setStyleSheet('''
            QWidget#right_widget{
                color:#232C51;
                background:white;
                border-top:1px solid white;
                border-bottom:1px solid white;
                border-right:1px solid white;
                border-top-right-radius:10px;
                border-bottom-right-radius:10px;
            }
            QLabel#right_label{
                border:none;
                font-size:15px;
                font-weight:700;
                font-family:Helvetica, Arial, sans-serif;
            }
        ''')

        # 操作栏
        self.system_widget = QtWidgets.QWidget()
        self.system_layout = QtWidgets.QGridLayout()
        self.system_widget.setLayout(self.system_layout)
        # 关闭按钮
        self.right_close = QtWidgets.QPushButton("×")
        self.right_close.setFixedSize(20, 20)
        self.right_close.setStyleSheet(
            '''QPushButton{background:#F76677;border-radius:5px;}QPushButton:hover{background:red;}''')
        # 空白按钮
        self.right_visit = QtWidgets.QPushButton("□")
        self.right_visit.setFixedSize(20, 20)
        self.right_visit.clicked.connect(self.max_window)
        self.right_visit.setStyleSheet(
            '''QPushButton{background:#F7D674;border-radius:5px;}QPushButton:hover{background:yellow;}''')
        # 最小化按钮
        self.right_mini = QtWidgets.QPushButton("-")
        self.right_mini.setFixedSize(20, 20)
        self.right_mini.setCheckable(True)
        self.right_mini.clicked.connect(self.mini_window)
        self.right_mini.setStyleSheet(
            '''QPushButton{background:#6DDF6D;border-radius:5px;}QPushButton:hover{background:green;}''')
        self.system_layout.addWidget(self.right_mini, 0, 0, 1, 1)
        self.system_layout.addWidget(self.right_visit, 0, 1, 1, 1)
        self.system_layout.addWidget(self.right_close, 0, 2, 1, 1)
        self.right_layout.addWidget(self.system_widget, 0, 8, 1, 1)

        self.right_recommend_label = QtWidgets.QLabel("推荐歌曲")
        self.right_recommend_label.setObjectName('right_label')

        # 推荐封面部件
        self.right_recommend_widget = QtWidgets.QWidget()
        # 推荐封面网格布局
        self.right_recommend_layout = QtWidgets.QGridLayout()
        self.right_recommend_widget.setLayout(self.right_recommend_layout)

        self.lists = utils.get_music_name('lyr_pic_song/Music/')
        random.shuffle(self.lists)
        self.recommend_button = []
        self.music_list_tuijian = []
        for i in range(0, 5):
            self.recommend_button.append(QtWidgets.QToolButton())
            self.music_list_tuijian.append(self.lists[i])
            # 设置按钮文本
            self.recommend_button[i].setText(self.lists[i][0:12]+'...')
            # 设置默认按钮图标
            self.recommend_button[i].setIcon(QtGui.QIcon(r'lyr_pic_song/歌手写真/' + self.lists[i] + '.jpg'))
            self.recommend_button[i].setIconSize(QtCore.QSize(100, 100))
            self.recommend_button[i].setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
            self.right_recommend_layout.addWidget(self.recommend_button[i], 0, i)
        self.recommend_button[0].clicked.connect(lambda: self.music_play_single(music_name=self.lists[0]))
        self.recommend_button[1].clicked.connect(lambda: self.music_play_single(music_name=self.lists[1]))
        self.recommend_button[2].clicked.connect(lambda: self.music_play_single(music_name=self.lists[2]))
        self.recommend_button[3].clicked.connect(lambda: self.music_play_single(music_name=self.lists[3]))
        self.recommend_button[4].clicked.connect(lambda: self.music_play_single(music_name=self.lists[4]))

        self.right_layout.addWidget(self.right_recommend_label, 1, 0, 1, 9)
        self.right_layout.addWidget(self.right_recommend_widget, 2, 0, 2, 9)

        self.right_newsong_label = QtWidgets.QLabel("本地歌曲")
        self.right_newsong_label.setObjectName('right_label')

        self.right_playlist_label = QtWidgets.QLabel("热门歌曲")
        self.right_playlist_label.setObjectName('right_label')

        # 本地歌曲部件
        self.right_newsong_widget = QtWidgets.QWidget()
        # 本地歌曲部件网格布局
        self.right_newsong_layout = QtWidgets.QGridLayout()
        self.right_newsong_widget.setLayout(self.right_newsong_layout)

        # 展示本地歌曲
        self.music_list = QtWidgets.QListWidget()
        self.music_list.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.music_list.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.music_list.doubleClicked.connect(lambda: self.music_play())
        lists = utils.get_music_name('lyr_pic_song/Music/')
        for i in lists:
            # 把字符串转化为QListWidgetItem项目对象
            self.item = QtWidgets.QListWidgetItem(i)
            # 添加项目
            self.music_list.addItem(self.item)
        self.right_newsong_layout.addWidget(self.music_list, 0, 0, 6, 1)

        # 热门歌单部件
        self.right_playlist_widget = QtWidgets.QWidget()
        # 热门歌单网格布局
        self.right_playlist_layout = QtWidgets.QGridLayout()
        self.right_playlist_widget.setLayout(self.right_playlist_layout)

        self.playlist_button_1 = QtWidgets.QToolButton()
        self.playlist_button_1.setText("说好不哭" + "\n\n" + "周杰伦")
        self.playlist_button_1.setIcon(QtGui.QIcon('lyr_pic_song/歌手写真/周杰伦.jpg'))
        self.playlist_button_1.setIconSize(QtCore.QSize(100, 75))
        self.playlist_button_1.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.playlist_button_1_music = '说好不哭'
        self.playlist_button_1.clicked.connect(lambda: self.music_play_single(music_name=self.playlist_button_1_music))

        self.playlist_button_2 = QtWidgets.QToolButton()
        self.playlist_button_2.setText("野狼Disco" + "\n\n" + "宝石GEM")
        self.playlist_button_2.setIcon(QtGui.QIcon('lyr_pic_song/歌手写真/宝石GEM.jpg'))
        self.playlist_button_2.setIconSize(QtCore.QSize(100, 75))
        self.playlist_button_2.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.playlist_button_2.clicked.connect(lambda: self.music_play_single(music_name='野狼Disco'))

        self.playlist_button_3 = QtWidgets.QToolButton()
        self.playlist_button_3.setText("雅俗共赏" + "\n\n" + "许嵩")
        self.playlist_button_3.setIcon(QtGui.QIcon('lyr_pic_song/歌手写真/许嵩.jpg'))
        self.playlist_button_3.setIconSize(QtCore.QSize(100, 75))
        self.playlist_button_3.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.playlist_button_3.clicked.connect(lambda: self.music_play_single(music_name='雅俗共赏'))

        self.playlist_button_4 = QtWidgets.QToolButton()
        self.playlist_button_4.setText("画(Live Piano Seesion Ⅱ)" + "\n\n" + "G.E.M.邓紫棋")
        self.playlist_button_4.setIcon(QtGui.QIcon('lyr_pic_song/歌手写真/邓紫棋.jpg'))
        self.playlist_button_4.setIconSize(QtCore.QSize(100, 75))
        self.playlist_button_4.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.playlist_button_4.clicked.connect(lambda: self.music_play_single(music_name='画(Live Piano Seesion Ⅱ)'))

        self.right_playlist_layout.addWidget(self.playlist_button_1, 0, 0)
        self.right_playlist_layout.addWidget(self.playlist_button_2, 0, 1)
        self.right_playlist_layout.addWidget(self.playlist_button_3, 1, 0)
        self.right_playlist_layout.addWidget(self.playlist_button_4, 1, 1)
        self.right_layout.addWidget(self.right_newsong_label, 4, 0, 1, 5)
        self.right_layout.addWidget(self.right_playlist_label, 4, 5, 1, 4)
        self.right_layout.addWidget(self.right_newsong_widget, 5, 0, 1, 5)
        self.right_layout.addWidget(self.right_playlist_widget, 5, 5, 1, 4)

        # 美化歌曲列表
        self.right_recommend_widget.setStyleSheet(
            '''
                QToolButton{border:none;}
                QToolButton:hover{border-bottom:2px solid #F76677;}
            ''')
        self.right_playlist_widget.setStyleSheet(
            '''
                QToolButton{border:none;}
                QToolButton:hover{border-bottom:2px solid #F76677;}
            ''')
        self.right_newsong_widget.setStyleSheet('''
            QListWidget{
                border:none;
                color:gray;
                font-size:13px;
                height:45px;
                padding-left:5px;
                text-align:left;
            }
            QListWidget::item:hover{
                color:black;
                border:1px solid #F3F3F5;
                border-radius:10px;
                background:LightGray;
            }
        ''')

        # 播放进度部件
        self.right_process_bar = QtWidgets.QProgressBar()
        # 设置进度条高度
        self.right_process_bar.setFixedHeight(2)
        # 不显示进度条文字
        self.right_process_bar.setTextVisible(False)

        # 播放控制部件
        self.right_playconsole_widget = QtWidgets.QWidget()
        # 播放控制部件网格布局层
        self.right_playconsole_layout = QtWidgets.QGridLayout()
        self.right_playconsole_widget.setLayout(self.right_playconsole_layout)

        # 正在播放
        self.music_pic = QtWidgets.QToolButton()
        self.music_pic.setText("        " + "\n\n" + "        ")
        self.music_pic.setIcon(QtGui.QIcon('images/专辑.jpg'))
        self.music_pic.setIconSize(QtCore.QSize(60, 60))
        self.music_pic.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)

        # 随机播放按钮
        self.random_play = QtWidgets.QPushButton(qtawesome.icon('fa.random', color='#F76677'), "")
        self.random_play_flag = 1
        self.random_play.clicked.connect(self.play_order)
        self.random_play.setObjectName('random_play')
        # 音量按钮
        self.music_volume = QtWidgets.QPushButton(qtawesome.icon('fa.volume-up', color='#F76677'), "")
        # 上一曲按钮
        self.console_button_1 = QtWidgets.QPushButton(qtawesome.icon('fa.backward', color='#F76677'), "")
        self.console_button_1.clicked.connect(self.backward)
        # 下一曲按钮
        self.console_button_2 = QtWidgets.QPushButton(qtawesome.icon('fa.forward', color='#F76677'), "")
        self.console_button_2.clicked.connect(self.forward)
        # 播放/暂停按钮
        self.console_button_3 = QtWidgets.QPushButton(qtawesome.icon('fa.play', color='#F76677', font=18), "")
        self.console_button_3_flag = 1
        self.console_button_3.clicked.connect(self.play_stop)
        self.console_button_3.setIconSize(QtCore.QSize(30, 30))
        # 歌词显示按钮
        self.console_button_4 = QtWidgets.QPushButton(qtawesome.icon('fa.music', color='#AAAAAA', font=18), "")
        self.console_button_4.clicked.connect(self.lyric_show)
        self.console_button_4_flag = 1

        # 设置已播放时间
        self.music_time_play = QtWidgets.QLabel('00:00' + ' /')
        self.music_time_play.setObjectName('music_time_play')
        # 设置音乐总时间
        self.music_time_all = QtWidgets.QLabel('00:00')

        self.right_playconsole_layout.addWidget(self.console_button_1, 0, 2)
        self.right_playconsole_layout.addWidget(self.console_button_2, 0, 4)
        self.right_playconsole_layout.addWidget(self.console_button_3, 0, 3)
        self.right_playconsole_layout.addWidget(self.console_button_4, 0, 6)
        self.right_playconsole_layout.addWidget(self.random_play, 0, 1)
        self.right_playconsole_layout.addWidget(self.music_volume, 0, 5)
        self.right_playconsole_layout.addWidget(self.music_pic, 0, 0)
        self.right_playconsole_layout.addWidget(self.music_time_play, 0, 7)
        self.right_playconsole_layout.addWidget(self.music_time_all, 0, 8)

        # 播放按钮样式
        self.right_process_bar.setStyleSheet('''
            QProgressBar::chunk {
                background-color: #F76677;
            }
        ''')

        self.right_playconsole_widget.setStyleSheet('''
            QPushButton{
                border:none;
            }
            QToolButton{
                border:none;
                font-family: Helvetica, Arial, sans-serif;
            }
            QPushButton#random_play{
                margin-left:100px;
            }
            QLabel#music_time_play{
                margin-left:100px;
            }
        ''')

        self.right_layout.addWidget(self.right_process_bar, 9, 0, 1, 9)
        self.right_layout.addWidget(self.right_playconsole_widget, 10, 0, 1, 9)

    # 窗口最小化
    def mini_window(self):
        if self.right_mini.isChecked():
            self.right_mini.setCheckable(False)
            self.setWindowState(QtCore.Qt.WindowMinimized)
        self.right_mini.setCheckable(True)

    # 窗口最大化
    def max_window(self):
        if self.isFullScreen():
            self.setWindowState(QtCore.Qt.WindowNoState)
        else:
            self.setWindowState(QtCore.Qt.WindowFullScreen)

    # 设置播放顺序
    def play_order(self):
        # 设置为循环播放
        if self.random_play_flag == 1:
            self.random_play.setIcon(qtawesome.icon('fa.retweet', color='#F76677'))
            self.random_play_flag = 2
        # 设置为单曲循环
        elif self.random_play_flag == 2:
            self.random_play.setIcon(qtawesome.icon('fa.refresh', color='#F76677'))
            self.random_play_flag = 3
        # 设置为随机播放
        else:
            self.random_play.setIcon(qtawesome.icon('fa.random', color='#F76677'))
            self.random_play_flag = 1

    # 设置播放/暂停
    def play_stop(self):
        # print(self.music_list.currentRow())
        # 设置为播放
        if self.console_button_3_flag == 1:
            self.console_button_3.setIcon(qtawesome.icon('fa.pause', color='#F76677'))
            self.console_button_3_flag = 2
            # if int(self.music_list.currentRow()) == -1:
            #     self.forward()
            # else:
            pygame.mixer.music.unpause()
            self.t = Thread(target=self.progress_bar_show)
            self.t.start()
        # 设置为暂停
        else:
            self.console_button_3.setIcon(qtawesome.icon('fa.play', color='#F76677'))
            self.console_button_3_flag = 1
            pygame.mixer.music.pause()

    # 搜索音乐
    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Enter:
            message = self.right_bar_widget_search_input.text()
            auto_download = ad.auto_download(r'lyr_pic_song\Music')
            if message == '':
                music_dic = {'message': '无搜索结果'}
            else:
                # 根据搜索关键字爬取网易云音乐
                music_dic = auto_download.search(self.right_bar_widget_search_input.text())
            dialogWindow.DialogWindow(music_dic, auto_download)

    # 单击歌曲播放
    def music_play_single(self, music_name):
        # 如果桌面歌词正在显示，则调用歌词显示方法
        if self.console_button_4_flag == 2:
            self.console_button_4_flag = 1
            self.lyric_show()
        # 如果有歌曲正在播放，则先将该歌曲停止播放
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.stop()
        pygame.mixer.music.load(r'lyr_pic_song\Music\\' + music_name + '.mp3')
        pygame.mixer.music.play(1, 0.0)
        time.sleep(0)
        str_music = music_name.split('-')
        self.music_pic.setText(str_music[1] + '...' + '\n\n' + str_music[0] + '...')
        self.music_pic.setIcon(QtGui.QIcon(r'lyr_pic_song/歌手写真/' + music_name
                                           + '.jpg'))

        # 将播放按钮修改为暂停按钮
        self.console_button_3.setIcon(qtawesome.icon('fa.pause', color='#F76677'))
        self.console_button_3_flag = 2
        # 计算进度条的值
        audio = MP3(r'lyr_pic_song\Music\\' + music_name + '.mp3')
        self.all_time = audio.info.length
        self.right_process_bar.setRange(0, self.all_time)
        self.music_time_all.setText(str("%.2d" % int(self.all_time / 60)) + ':' + str("%.2d" % int(self.all_time % 60)))

        self.t = Thread(target=self.progress_bar_show, args=(self.music_list.currentRow(),))
        self.t.start()

    # 双击歌曲列表的音乐播放音乐
    def music_play(self):
        # 如果桌面歌词正在显示，则调用歌词显示方法
        if self.console_button_4_flag == 2:
            self.console_button_4_flag = 1
            self.lyric_show()
        # 如果有歌曲正在播放，则先将该歌曲停止播放
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.stop()
        pygame.mixer.music.load(r'lyr_pic_song\Music\\' + self.music_list.currentItem().text() + '.mp3')
        pygame.mixer.music.play(1, 0.0)
        time.sleep(0)
        str_music = str(self.music_list.currentItem().text()).split('-')
        self.music_pic.setText(str_music[1][0:12] + '...' + '\n\n' + str_music[0][0:12] + '...')
        self.music_pic.setIcon(QtGui.QIcon(r'lyr_pic_song/歌手写真/' + self.music_list.currentItem().text()
                                           + '.jpg'))

        # 将播放按钮修改为暂停按钮
        self.console_button_3.setIcon(qtawesome.icon('fa.pause', color='#F76677'))
        self.console_button_3_flag = 2
        # 计算进度条的值
        audio = MP3(r'lyr_pic_song\Music\\' + self.music_list.currentItem().text() + '.mp3')
        self.all_time = audio.info.length
        self.right_process_bar.setRange(0, self.all_time)
        self.music_time_all.setText(str("%.2d" % int(self.all_time / 60)) + ':' + str("%.2d" % int(self.all_time % 60)))
        self.t = Thread(target=self.progress_bar_show, args=(self.music_list.currentRow(),))
        self.t.start()

    # 歌曲进度条自动前进
    def progress_bar_show(self, row):
        while True:
            if self.console_button_3_flag == 2 and row == self.music_list.currentRow():
                played = float(pygame.mixer.music.get_pos()) / 1000
                self.right_process_bar.setValue(played)
                self.music_time_play.setText(str("%.2d" % int(played / 60)) + ':' + str("%.2d" % int(played % 60))
                                             + ' /')
            else:
                break

    # 上一曲
    def backward(self):
        self.music_list.setCurrentRow(self.music_list.currentRow() - 1)
        self.music_play()

    # 下一曲
    def forward(self):
        self.music_list.setCurrentRow(self.music_list.currentRow() + 1)
        self.music_play()

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

    # 歌词显示
    def lyric_show(self):
        # 显示歌词
        if self.console_button_4_flag == 1:
            self.console_button_4.setIcon(qtawesome.icon('fa.music', color='#F76677', font=18))
            self.console_button_4_flag = 2
            if self.music_list.currentRow() == -1:
                self.lyric_win = lyricWindow.LyricWindow('')
            else:
                self.lyric_win = lyricWindow.LyricWindow(r'lyr_pic_song/Music/'
                                                         + self.music_list.currentItem().text() + '.mp3')
            self.lyric_win.show()
            self.lyric_t = Thread(target=self.set_lyric, args=(self.music_list.currentRow(),))
            self.lyric_t.start()
            # print('1-->' + str(self.lyric_t.ident))
            # Thread(target=self.lyric_show_child).start()
        # 隐藏歌词
        else:
            self.console_button_4.setIcon(qtawesome.icon('fa.music', color='#AAAAAA', font=18))
            self.console_button_4_flag = 1
            self.lyric_win.hide()

    # 更新歌词
    def set_lyric(self, row):
        while True:
            if self.console_button_3_flag == 2 and row == self.music_list.currentRow():
                self.lyric_win.set_lyric(pygame.mixer.music.get_pos())
            else:
                break


def main():
    app = QtWidgets.QApplication(sys.argv)
    gui = MainUi()
    gui.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
