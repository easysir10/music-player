# -*- coding: UTF-8 -*-

import pygame

lrcDict = {}
allTimeList = []


# 读取歌词文件
def getLrc(filePath):
    lrcFile = filePath.split(".")[0] + ".lrc"
    # print(lrcFile)
    try:
        fo = open(lrcFile, "r", encoding="GBK")  # 打开一个文件，r为只读模式
        lrcStr = fo.read()  # 从打开文件中读取一个字符串
        # print(lrcStr)
        return lrcStr
    except FileNotFoundError:
        return ""


# 将歌词拆分成字典类型，时间戳为key，歌词为value
def splitLrc(filePath):
    lrcList = getLrc(filePath).splitlines()
    for lrcLine in lrcList:
        lrcLineList = lrcLine.split("]")
        for index in range(len(lrcLineList) - 1):
            timeStr = lrcLineList[index][1:]
            secs = revertTime(timeStr)
            if secs == -1:
                break
            lrcDict[secs] = lrcLineList[-1]
    getLrcTime()
    # getLrcWord()


# 将时间戳转换成秒
def revertTime(timeStr):
    # print(timeStr, end="   ")
    timeList = timeStr.split(":")
    if timeList[0].isdigit():
        secs = round(float(timeList[0]) * 60 + float(timeList[1]), 2)
    else:
        secs = -1
    # print(secs)
    return secs


# 将字典中的歌词时间提取出来，存储到list中
def getLrcTime():
    global allTimeList
    for t in lrcDict:
        allTimeList.append(t)
    allTimeList.sort()
    # print(allTimeList)

# # 按时间打印歌词
# def printLrc(filePath):
#     global lrcDict
#     global allTimeList
#     for key in allTimeList:
#         while True:
#             end_time = round(float(pygame.mixer.music.get_pos()) / 1000, 2)
#             if end_time == key:
#                 print(key, lrcDict[key])
#                 break


# def main():
#     path = "D:/Course/aliyun/week02/code/music/"
#     # fileName = "周深 - 亲爱的旅人啊 (Cover_ 木村弓).mp3"
#     fileName = "Robbie Williams - She's The One.mp3"
#     filePath = path + fileName
#
#     splitLrc(filePath)
#     for key in lrcDict:
#         print(key, lrcDict[key])
#
#
# main()
