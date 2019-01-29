from gevent.queue import Queue
from gevent import monkey
monkey.patch_all()
import gevent,requests, bs4, csv,time
start = time.time()
url_list=['http://www.boohee.com/food/group/{0}?page={1}'.format(i,j) for i in range(1,4)for j in range(1,4)]
#print(url_list)
for i in range(1,4):
    url_list.append('http://www.boohee.com/food/view_menu?page={}'.format(i))
#print(url_list)

work = Queue()
for url in url_list:
    work.put_nowait(url)

def crawler():
    while not work.empty():
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
        }
        url = work.get_nowait()
        r = requests.get(url,headers=headers)
        #print(url,work.qsize(),r.status_code)
        bs=bs4.BeautifulSoup(r.text,'html.parser')
        list=bs.find('ul',class_="food-list").find_all('li')
        #print(list)
        for i in list:
            print(i.select('.text-box a')[0].text)
            print(i.find('p').text)
            print('-----------')
tasks_list  = [ ]

#等于建立两个爬虫
for x in range(5):
    task = gevent.spawn(crawler)
    tasks_list.append(task)
gevent.joinall(tasks_list)

end = time.time()
print(end-start)