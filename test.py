def test1():
    for i in range(3):
        a=int(input('你猜多大：'))
        if a==24:
            print('猜对了')
            break
        elif a>24:
            print('第{}次，大了'.format(i+1))
        else:
            print('第{}次，小了'.format(i+1))
    else:
        print('猜3次了')
def test2():
    for i in range(3):
        a = int(input('你猜多大'))
        if a == 24:
            print('猜对了')
            exit()
        elif a > 24:
            print('大了')
            continue
        else:
            print('小了')
            continue
    print('猜3次了')

test1()
