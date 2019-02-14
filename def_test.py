#[print(n,end=' ') for n in range(1,8) if n!=4]
def test(n):
    if n<8:
        if n!=4:
            print(n,end=' ')
        return test(n+1)
test(1)