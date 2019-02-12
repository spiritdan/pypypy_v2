def find_all_index(arr,item):
    return [i for i,a in enumerate(arr) if a==item]
list=[1,2,3,3,4,4,5,6]
print(find_all_index(list,3))
with open('123.jpg','rb') as f:
    print(f.read())
f.close

import re

# \d+ 匹配字符串中的数字部分，返回列表

ss = '全部共 103920 条'
num = re.findall('\d+',ss)[0]
print(num)
num = 103919
if num%20==0:
    page_num=num/20
else:
    page_num=int(num/20)+1
print(page_num)
a=1


for i in range(3):
    if i==2:
        break
    print(i)
else:
    print('3次结束')

punches = ['石头','剪刀','布']
print(punches[-3])

a=[1,2,3]
b=a
a[1]=6
print(b)

b=a[:]
a[0]=3
print(b)