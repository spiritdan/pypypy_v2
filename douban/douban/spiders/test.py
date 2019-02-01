import bs4
import requests
import re


def parse():
    response=requests.get('https://book.douban.com/top250?start=0')
    bs = bs4.BeautifulSoup(response.text, 'html.parser')
    print(bs.text)
    div_list = bs.find_all('div',class_="pl2")
    print(div_list)
    for div in div_list:
        link = div.find('a')['href']
        print(link)
def parse_book():
    # 定义新的处理response的方法parse_job（方法的名字可以自己起）
    response = requests.get('https://book.douban.com/subject/1770782/')
    bs = bs4.BeautifulSoup(response.text, 'html.parser')
    # 用BeautifulSoup解析response(公司招聘信息的网页源代码)
    shot_comment_url = bs.find('div',class_="mod-hd").find('span',class_="pl").find('a')['href']
    print(shot_comment_url)
def parse_comment():
    response = requests.get('https://book.douban.com/subject/1770782/comments/')
    bs = bs4.BeautifulSoup(response.text, 'html.parser')

    comments=bs.find('span',id='total-comments').text
    num = int(re.findall('\d+', comments)[0])
    if num%20==0:
        page_num=num/20
    else:
        page_num=int(num/20)+1
    for i in range(1,page_num+1):
        final_url='https://book.douban.com/subject/1770782/comments/hot?p={0}'.format(i)
        print(final_url)

def parse_comment_details():
    response = requests.get('https://book.douban.com/subject/1770782/comments/hot?p=5093')

    bs = bs4.BeautifulSoup(response.text, 'html.parser')
    print(bs.text)
    list_comments = bs.find_all('li', class_='comment-item')
    print(list_comments)
    for comment in list_comments:
        user = comment.find('span', class_='comment-info').find('a').text.strip()
        date_list = comment.find('span', class_='comment-info').find_all('span')
        if len(date_list)>1:
            date=date_list[1].text
        else:
            date = date_list[0].text
        content= comment.find('p',class_='comment-content').text.strip()
        print(user,date,content)
#parse()
#parse_book()
#parse_comment()
parse_comment_details()