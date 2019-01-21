print(5*" ",end='')
print(1*"*")

print(4*" ",end='')
print(3*"*")

print(3*" ",end='')
print(5*"*")

print(2*" ",end='')
print(7*"*")

print(1*" ",end='')
print(9*"*")

again=True
while again:
    a = input('是否继续？Y/N')

    if a.lower()=='N':
        again=False
else:
    print('你选择了N')