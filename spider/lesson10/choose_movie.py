from urllib.request import quote
import requests, random, csv, time
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText
from email.header import Header


def get_movies():
    csv_file = open('movieTop.csv', 'w', newline='', encoding='utf-8')
    writer = csv.writer(csv_file)

    for x in range(10):
        url = 'https://movie.douban.com/top250?start=' + str(x * 25) + '&filter='
        res = requests.get(url)
        bs = BeautifulSoup(res.text, 'html.parser')
        bs = bs.find('ol', class_="grid_view")
        for titles in bs.find_all('li'):
            title = titles.find('span', class_="title").text
            list1 = [title]
            writer.writerow(list1)
    csv_file.close()


def get_link(movie):
    try:
        movie_gbk = movie.encode('gbk')
        url = 'http://s.ygdy8.com/plus/so.php?kwtype=0&searchtype=title&keyword=' + quote(movie_gbk)
        req = requests.get(url)
        bsmovie = BeautifulSoup(req.text, 'html.parser')
        link = bsmovie.select('.co_content8 b a')
        finallink = 'http://www.ygdy8.com' + link[0].get('href')
        # print(finallink)
        req = requests.get(finallink).content.decode('gbk')
        bsmovie2 = BeautifulSoup(req, 'html.parser')
        movie_link = bsmovie2.select('.co_content8 table tbody  a')
        link = ''
        for i in range(0, len(movie_link)):
            # 延迟三秒，方式封IP
            link = '链接' + str(i) + ":" + movie_link[i].get('href')
            time.sleep(1)
    except:
        link='无'

    return link


def sendmail(text, receiver, account, password):
    qqmail = smtplib.SMTP_SSL('smtp.qq.com', 465)
    qqmail.login(account, password)
    # 以上，是登录邮箱
    theme = '食谱'

    sender = 'william'
    # 以上，是输入内容
    message = MIMEText(text, 'plain', 'utf-8')
    message['Subject'] = Header(theme, 'utf-8')
    message['From'] = Header(sender, 'utf-8')
    message['To'] = Header(receiver)
    # 以上，是一波转换操作

    try:
        qqmail.sendmail(account, receiver, message.as_string())
        print(receiver + '邮件已发送')
    except:
        print('对不起，发送失败请重试！')
    qqmail.quit()
    print('邮件已完成发送')


if __name__ == "__main__":
    get_movies()
    movie_list = []
    link_dic = {}
    with open('movieTop.csv', 'r', encoding='utf8') as f:
        reader = csv.reader(f)
        for row in reader:
            print(row[0])
            movie_list.append(row[0])
        print(movie_list)
    random_movies = random.sample(movie_list, 3)
    print(random_movies)

    for movie in random_movies:
        link = get_link(movie)
        link_dic[movie] = link
    print(link_dic)

''' 
    account = input('请输入你的QQ邮箱：')
    password = input('请输入你的邮箱密码：')
    receiver = input('请输入你的发送地址：')
    sendmail(text, receiver, account, password)
'''