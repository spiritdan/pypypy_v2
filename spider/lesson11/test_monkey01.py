import gevent,time,requests
from gevent import monkey
monkey.patch_all()

start = time.time()

url_list = ['https://www.baidu.com/',
'https://www.sina.com.cn/',
'http://www.sohu.com/',
'https://www.qq.com/',
'https://www.163.com/',
'http://www.iqiyi.com/',
'https://www.tmall.com/',
'http://www.ifeng.com/']

def crawler(url):
    r = requests.get(url)
    print(url,time.time()-start,r.status_code)

tasks_list = []

for url in url_list:
    task = gevent.spawn(crawler,url)
    tasks_list.append(task)
gevent.joinall(tasks_list)