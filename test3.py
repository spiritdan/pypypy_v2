again=True;again2=3;print(again,again2)
while again:
    a = input('是否继续？Y/N')

    if a.lower()=='N':
        again=False
else:
    print('你选择了N')