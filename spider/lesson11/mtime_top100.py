# -*- coding: utf-8 -*-
from gevent.queue import Queue
from gevent import monkey
monkey.patch_all()
import gevent,time,requests,bs4,csv

def write_csv(movie_dict):
    csv_file = open('mtime_top100.csv', 'w', newline='',encoding='utf8')

    writer = csv.writer(csv_file)
    writer.writerow(['排名','链接','简介'])
    for k,value in movie_dict.items():
        writer.writerow([k]+value)
    csv_file.close()


start = time.time()
url_list=['http://www.mtime.com/top/tv/top100/index-{0}.html'.format(i) for i in range(1,11)]
url_list[0]=('http://www.mtime.com/top/tv/top100/index.html')
print(url_list)

work = Queue()
for url in url_list:
    work.put_nowait(url)
movie_dict={}
def crawler():
    while not work.empty():
        url = work.get_nowait()
        r = requests.get(url)
        print(url,work.qsize(),r.status_code)
        bs=bs4.BeautifulSoup(r.text,'html.parser')
        movie_list=bs.find('ul',id="asyncRatingRegion").find_all('li')
        print(movie_list)

        for movie in movie_list:
            movie_tmp=[]
            movie_info=movie.find_all('div')
            print(movie_info[0].text)
            print(movie_info[1].find('a')["href"])
            print(movie_info[2].text)
            movie_tmp.append(movie_info[1].find('a')["href"])
            movie_tmp.append(movie_info[2].text)
            movie_dict[movie_info[0].text]=movie_tmp

tasks_list  = [ ]

#等于建立两个爬虫
for x in range(5):
    task = gevent.spawn(crawler)
    tasks_list.append(task)
gevent.joinall(tasks_list)

end = time.time()
print('爬取时间时间：{0}'.format(end-start))
print(movie_dict)
end2 = time.time()
write_csv(movie_dict)
print('文件写入时间：{0}'.format(end2-end))