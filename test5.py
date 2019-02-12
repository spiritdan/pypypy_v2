
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
m=['Diamond','Heart','club','spade']
i=[x for x in range(1,14)]
def cards():
    for suit in m:
        for num in i:
            #print((suit,num))
            yield suit,num
#for x in cards():
#    print(x)

def cards2():
    a = []
    for suit in m:
        for num in i:
            a.append((suit,num))
    return a
l=cards2()
print(l)