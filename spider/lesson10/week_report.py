import requests
from bs4 import BeautifulSoup
import smtplib, time
from email.mime.text import MIMEText
from email.header import Header
import schedule
import time


def get_foodlist():
    res_foods = requests.get('http://www.xiachufang.com/explore/')
    bs_foods = BeautifulSoup(res_foods.text,'html.parser')
    list_foods = bs_foods.find_all('div',class_='info pure-u')

    list_all = []

    for food in list_foods:
        tag_a = food.find('a')
        name = tag_a.text[17:-13]
        URL = 'http://www.xiachufang.com'+tag_a['href']
        tag_p = food.find('p',class_='ing ellipsis')
        ingredients = tag_p.text[1:-1]
        list_all.append([name,URL,ingredients])
    print(list_all)
    return list_all

qqmail = smtplib.SMTP_SSL('smtp.qq.com', 465)


def sendmail(text,receiver, account, password):
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

def job():
    print("I'm working...")
    food_list = get_foodlist()
    tmp_list = []
    for i in food_list:
        tmp_list.append('\n'.join(i))
    text = '\n-----------------------------\n'.join(tmp_list)
    print(text)
    sendmail(text, receiver, account, password)


if __name__ == "__main__":
    #food_list=get_foodlist()
    #tmp_list=[]
    #for i in food_list:
    #    tmp_list.append('\n'.join(i))
    #text='\n-----------------------------\n'.join(tmp_list)
    #print(text)
    account = input('请输入你的QQ邮箱：')
    password = input('请输入你的邮箱密码：')
    receiver = input('请输入你的发送地址：')
    #sendmail(text, receiver, account, password)
    schedule.every().thursday.at("12:52").do(job)

    while True:
        schedule.run_pending()
        time.sleep(1)