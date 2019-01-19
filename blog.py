import requests
import bs4
res = requests.get('https://wordpress-edu-3autumn.localprod.forc.work/all-about-the-future_04/')
bs=bs4.BeautifulSoup(res.text,'html.parser')
comment_list=bs.find_all(class_='comment-body')
for comment in comment_list:
    user=comment.find(class_='fn').getText()
    time=comment.find('time').getText().strip()
    content=comment.find(class_='comment-content').getText()
    print('{0}在{1}说道：{2}'.format(user,time,content))