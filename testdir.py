import os
path = "C:\\test\\"
dirs = os.listdir(path)

list=[]
for i in dirs:
    if os.path.splitext(i)[1] == ".txt":
        print(i)
        with open(path+i,'r') as f:
            for i in f.readlines():
                list.append(i[:11]+'\n')
        f.close()
print(list)

with open('合并.txt', 'w+') as f:
    for j in list:
        f.write(j)
f.close()

