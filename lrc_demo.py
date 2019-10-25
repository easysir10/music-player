# -*- coding: UTF-8 -*-
import ctypes
import time
import pygame
import threading
import tkinter
import os
import inspect

lrcDict = {}
allTimeList = []

pygame.mixer.init()
# 创建主窗口
win = tkinter.Tk()
# 设置标题
win.title("MusicPlayer")
# 设置大小和位置
win.geometry("600x400")
# 文本控件，用于显示多行文本
# 创建滚动条
scroll = tkinter.Scrollbar()
text = tkinter.Text(win, width=50, height=8)
# side放到窗体的那一侧   fill填充
scroll.pack(side=tkinter.RIGHT, fill=tkinter.Y)
text.pack(side=tkinter.LEFT, fill=tkinter.Y)
# 关联
scroll.config(command=text.yview)
text.config(yscrollcommand=scroll.set)


def start(filePath, musicThread):
    pygame.mixer.music.load(filePath)
    pygame.mixer.music.play(1, 0.0)
    musicThread.start()
    time.sleep(0)


def pause():
    pygame.mixer.music.pause()


def unpause():
    pygame.mixer.music.unpause()


def stop():
    pygame.mixer.music.stop()
    # get_thread()


# 读取歌词文件
def getLrc(filePath):
    lrcFile = filePath.split(".")[0] + ".lrc"
    # print(lrcFile)
    fo = open(lrcFile, "r", encoding="ISO-8859-1")  # 打开一个文件，r为只读模式
    lrcStr = fo.read()  # 从打开文件中读取一个字符串
    # print(lrcStr)
    return lrcStr


# 将歌词拆分成字典类型，时间戳为key，歌词为value
def splitLrc(filePath):
    global lrcDict
    lrcList = getLrc(filePath).splitlines()
    for lrcLine in lrcList:
        lrcLineList = lrcLine.split("]")
        for index in range(len(lrcLineList) - 1):
            timeStr = lrcLineList[index][1:]
            secs = revertTime(timeStr)
            lrcDict[secs] = lrcLineList[-1]
    getLrcTime()
    # getLrcWord()


# 将时间戳转换成秒
def revertTime(timeStr):
    # print(timeStr, end="   ")
    timeList = timeStr.split(":")
    secs = round(float(timeList[0]) * 60 + float(timeList[1]), 2)
    # print(secs)
    return secs


# 将字典中的歌词时间提取出来，存储到list中
def getLrcTime():
    global allTimeList
    for t in lrcDict:
        allTimeList.append(t)
    allTimeList.sort()
    # print(allTimeList)


# 按时间打印歌词
def printLrc(filePath):
    global lrcDict
    global allTimeList
    start_time = time.perf_counter()
    flag_music = 0
    for key in allTimeList:
        while True:
            end_time = round(time.perf_counter(), 2)
            if end_time == key:
                print(key, lrcDict[key])
                break


# 构建歌词面板
def drawLrcInterface(filePath):
    global text
    # 将歌词逐行添加到文本控件中
    for key in allTimeList:
        text.insert(tkinter.INSERT, lrcDict[key] + "\n")
    # 添加控制按钮
    musicThread = MusicThread()
    start(filePath, musicThread)
    button1 = tkinter.Button(win, text="开始", command=lambda: start(filePath, musicThread))
    button2 = tkinter.Button(win, text="暂停", command=pause)
    button3 = tkinter.Button(win, text="继续", command=unpause)
    button4 = tkinter.Button(win, text="停止", command=stop)
    button1.pack()
    button2.pack()
    button3.pack()
    button4.pack()


# 根据歌曲进度高亮当前歌词
def lineLight():
    # 根据歌曲进度高亮当前歌词
    flag_music = 0
    # for key in allTimeList:
    while flag_music < len(allTimeList):
        while True:
            # now_time = round(time.perf_counter(), 2)
            # 获取当前歌曲播放进度
            now_time = round(float(pygame.mixer.music.get_pos()) / 1000, 2)
            if now_time == allTimeList[flag_music]:
                # print(now_time, pygame.mixer.music.get_pos())
                # print(key, lrcDict[key])
                # 获取当前进度歌词内容的起始、结束位置，进行标亮
                start_position = str("%.2f" % float(flag_music + 1))
                end_position = str("%.2f" %
                                   (float(flag_music + 1) + float(len(lrcDict[allTimeList[flag_music]])) / 100))
                # print(start_position, end_position)
                print(len(lrcDict[allTimeList[flag_music]]))
                text.tag_add('newTag', start_position, end_position)
                text.tag_config('newTag', background='white', foreground='red')
                # 将上一句歌词内容格式清除
                if flag_music > 0:
                    old_start_position = str("%.2f" % float(flag_music))
                    old_end_position = str("%.2f" %
                                           (float(flag_music) + float(
                                               len(lrcDict[allTimeList[flag_music - 1]])) / 100))
                    text.tag_add('oldTag', old_start_position, old_end_position)
                    text.tag_config('oldTag', background='white', foreground='black')
                # 设置播放11行以后进行逐行向下滚动
                if flag_music > 11:
                    text.yview_scroll(1, 'units')
                break
        flag_music += 1

    # 控制台打印歌词线程
    # class lrcPlayThread(threading.Thread):
    #     def __init__(self, filePath):
    #         threading.Thread.__init__(self)
    #         self.filePath = filePath
    #
    #     def run(self):
    #         printLrc(self.filePath)


def _async_raise(tid, exctype):
    """raises the exception, performs cleanup if needed"""
    tid = ctypes.c_long(tid)
    if not inspect.isclass(exctype):
        exctype = type(exctype)
    res = ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, ctypes.py_object(exctype))
    if res == 0:
        raise ValueError("invalid thread id")
    elif res != 1:
        ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, None)
        raise SystemError("PyThreadState_SetAsyncExc failed")


def stop_thread(thread):
    _async_raise(thread.ident, SystemExit)


def get_thread():
    pid = os.getpid()
    while True:
        ts = threading.enumerate()
        print("------- Running threads On Pid: %d -------" % pid)
        for t in ts:
            print(t.name, t.ident, t.is_alive())
            if t.name == "music":
                print("I am go dying! Please take care of yourself and drink more hot water!")
                stop_thread(t)
        print(time.sleep(1))


class MusicThread(threading.Thread):
    def __init__(self):
        super(MusicThread, self).__init__()
        self.__stop_event = threading.Event()
        self.setName("music")

    def run(self):
        lineLight()


def main():
    path = "F:/MyDesktop/lyr_pic_song/Music/"
    fileName = "Why Don't We - I Still Do.mp3"
    filePath = path + fileName

    splitLrc(filePath)
    drawLrcInterface(filePath)
    win.mainloop()


main()
