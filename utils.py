# -*- coding: utf-8 -*-  
import os


def get_music_name(path):
    music_name_list = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if os.path.splitext(file)[1] == '.mp3':
                music_name_list.append(os.path.splitext(file)[0])
    return music_name_list


# lists = get_music_name('F:/MyDesktop/lyr_pic_song/Music/')
# for l in lists:
#     print(l)
