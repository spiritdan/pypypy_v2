import bs4, requests
from urllib.request import quote
import time
url = 'https://accounts.douban.com/j/mobile/login/basic'
headers={

"Host":"www.douban.com",

"User-Agent":"'Mozilla/5.0 (Windows NT 6.1; rv:53.0)Gecko/20100101 Firefox/53.0'",

"Accept-Language":"zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",

"Accept-Encoding":"gzip,deflate",

"Connection":"keep-alive"

}
data = {'ck': 'fzeS',
'name': '17706210570',
'password': '12ec0bc',
'remembe': 'false',
'ticket': ''}
#记录session
Soj_session = requests.session()
res = Soj_session.post(url, data=data, headers=headers)
time.sleep(1)
header2={'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
'Accept-Encoding': 'gzip, deflate, br',
'Accept-Language': 'zh-CN,zh;q=0.9',
'Connection': 'keep-alive',
'Host': 'fundin.douban.com',
'Referer': 'https://movie.douban.com/photos/photo/2545473122/',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
data2={
'download':'https://img3.doubanio.com/view/photo/raw/public/p2545473122.jpg',
'idsite':'100001',
'rec':'1',
'r':'353979',
'h':'14',
'm':'46',
's':'33',
'url':'https://movie.douban.com/photos/photo/2545473122/',
'urlref':'https://accounts.douban.com/passport/login',
'_id':'d872f03faef79255',
'_idts':'1548396492',
'_idvc':'1',
'_idn':'0',
'_refts':'1548396492',
'_viewts':'1548396492',
'_ref':'https://www.baidu.com/s?ie=UTF-8&wd=%E8%B1%86%E7%93%A3',
'pdf':'1',
'qt':'0',
'realp':'0',
'wma':'0',
'dir':'0',
'fla':'0',
'java':'0',
'gears':'0',
'ag':'0',
'cookie':'1',
'res':'1536x864',
'gt_ms':'198'
}
r=Soj_session.get('https://fundin.douban.com/piwik?download=https%3A%2F%2Fimg3.doubanio.com%2Fview%2Fphoto%2Fraw%2Fpublic%2Fp2545473122.jpg&idsite=100001&rec=1&r=353979&h=14&m=46&s=33&url=https%3A%2F%2Fmovie.douban.com%2Fphotos%2Fphoto%2F2545473122%2F&urlref=https%3A%2F%2Faccounts.douban.com%2Fpassport%2Flogin&_id=d872f03faef79255&_idts=1548396492&_idvc=1&_idn=0&_refts=1548396492&_viewts=1548396492&_ref=https%3A%2F%2Fwww.baidu.com%2Fs%3Fie%3DUTF-8%26wd%3D%25E8%25B1%2586%25E7%2593%25A3&pdf=1&qt=0&realp=0&wma=0&dir=0&fla=0&java=0&gears=0&ag=0&cookie=1&res=1536x864&gt_ms=198',data=data2, headers=header2)
with open('douban.jpg','wb')as f:
    f.write(r.content)
