from music_api import Music_api
from download import wangyiyun


class auto_download():
    def __init__(self, dir_path):
        self.dir_path = dir_path

    def search(self, str):
        list = Music_api().get_music_list(str)
        dic = {}
        for i in range(len(list)):
            song_dic = list[i]
            singer_dic = song_dic.get("ar")[0]
            song_id = song_dic.get("id")
            song_name = song_dic.get("name")
            singer_name = singer_dic.get("name")
            name = song_name + "-" + singer_name

            dic[song_id] = name

        return dic

    def download(self, song_id, name):
        d = wangyiyun()
        d.download_song(song_id, name, self.dir_path)
