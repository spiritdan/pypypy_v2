f=0.55
for i in range(64):
    f=f*2
    if f>1:
        print(1,end='')

        f=f-1
    else:
        print(0,end='')

