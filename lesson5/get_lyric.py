import requests
import html
import time
def get_Jay_music():
    # 引用requests模块
    res_music = requests.get('https://c.y.qq.com/soso/fcgi-bin/client_search_cp?ct=24&qqmusic_ver=1298&new_json=1&remoteplace=txt.yqq.song&searchid=60997426243444153&t=0&aggr=1&cr=1&catZhida=1&lossless=0&flag_qc=0&p=1&n=20&w=%E5%91%A8%E6%9D%B0%E4%BC%A6&g_tk=5381&loginUin=0&hostUin=0&format=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq.json&needNewCode=0')
    # 调用get方法，下载这个列表
    json_music = res_music.json()
    # 使用json()方法，将response对象，转为列表/字典
    list_music = json_music['data']['song']['list']
    # 一层一层地取字典，获取歌单列表
    for music in list_music:
    # list_music是一个列表，music是它里面的元素
        print(music['name'])
        # 以name为键，查找歌曲名
        print('所属专辑：'+music['album']['name'])
        # 查找专辑名
        print('播放时长：'+str(music['interval'])+'秒')
        # 查找播放时长
        url='https://y.qq.com/n/yqq/song/'+music['mid']+'.html'
        getlyric(url)
        time.sleep(1)
def getlyric(url):
    headers = {
        'origin': 'https://y.qq.com',
        # 请求来源，本案例中其实是不需要加这个参数的，只是为了演示
        'referer': 'https://y.qq.com/n/yqq/song/004Z8Ihr0JIu5s.html',
        # 请求来源，携带的信息比“origin”更丰富，本案例中其实是不需要加这个参数的，只是为了演示
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
        # 标记了请求从什么设备，什么浏览器上发出
    }
    param = {
        'nobase64': '1',
        'musicid': '212877900',
        '-': 'jsonp1',
        'g_tk': '5381',
        'loginUin': '0',
        'hostUin': '0',
        'format': 'json',
        'inCharset': 'utf8',
        'outCharset': 'utf - 8',
        'notice': '0',
        'platform': 'yqq.json',
        'needNewCode': '0'

    }
    res_lyric = requests.get('https://c.y.qq.com/lyric/fcgi-bin/fcg_query_lyric_yqq.fcg',headers=headers,params=param)
    res_lyric.encoding='utf8'
    lyric_json=res_lyric.json()
    print(lyric_json['lyric'])
    lyric_list = html.unescape(lyric_json['lyric'])
    print(lyric_list)

get_Jay_music()

