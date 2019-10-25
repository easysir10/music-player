import requests
import os
from scrapy.selector import Selector
import urllib.request


class wangyiyun():
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
            'Referer': 'http://music.163.com/'}
        self.main_url = 'http://music.163.com/'
        self.session = requests.Session()
        self.session.headers = self.headers

    def get_songurls(self, playlist):
        '''进入所选歌单页面，得出歌单里每首歌各自的ID 形式就是“song?id=64006"'''
        url = self.main_url + 'playlist?id=%d' % playlist
        re = self.session.get(url)  # 直接用session进入网页，懒得构造了
        sel = Selector(text=re.text)  # 用scrapy的Selector，懒得用BS4了
        songurls = sel.xpath('//ul[@class="f-hide"]/li/a/@href').extract()
        return songurls  # 所有歌曲组成的list
        ##['/song?id=64006', '/song?id=63959', '/song?id=25642714', '/song?id=63914', '/song?id=4878122', '/song?id=63650']

    def get_songinfo(self, songurl):
        '''根据songid进入每首歌信息的网址，得到歌曲的信息
        return：'64006'，'陈小春-失恋王'''
        url = self.main_url + songurl
        re = self.session.get(url)
        sel = Selector(text=re.text)
        song_id = url.split('=')[1]
        song_name = sel.xpath("//em[@class='f-ff2']/text()").extract_first()
        singer = '&'.join(sel.xpath("//p[@class='des s-fc4']/span/a/text()").extract())
        songname = singer + '-' + song_name
        return str(song_id), songname


    def download_song(self, song_id, songname, dir_path):
        '''根据歌曲url，下载mp3文件'''
        song_url = 'http://music.163.com/song/media/outer/url?id=%s.mp3' % song_id
        path = dir_path + os.sep + songname + '.mp3'  # 文件路径
        try:
            urllib.request.urlretrieve(song_url, path)  # 下载文件
            print("下载成功！")
        except:
            print("下载失败！")

