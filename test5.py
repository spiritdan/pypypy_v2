
def get_show():
    show()

def show():
    print(1)

get_show()
list=[1,2,'',4,'']
print(list)
import requests
url='https://book.douban.com/top250?start=0'
req=requests.get(url)
print(req.text)