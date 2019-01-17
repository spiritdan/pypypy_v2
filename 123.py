import requests
# 引用requests模块
from bs4 import BeautifulSoup
# 引用BeautifulSoup库

res_foods = requests.get('http://www.xiachufang.com/explore/')
# 获取数据
bs_foods = BeautifulSoup(res_foods.text,'html.parser')
# 解析数据
list_names = bs_foods.find_all('p',class_='name')
list_material = bs_foods.find_all('p',class_='ing ellipsis')
# 查找最小父级标签
food_list=[]
for i in range(0,len(list_names)):
    name=list_names[0].text.strip()
    url="http://www.xiachufang.com"+list_names[0].find('a')['href']
    #print(url)
    material=list_material[0].text.strip()
    food_list.append([name,url,material])
print(food_list)