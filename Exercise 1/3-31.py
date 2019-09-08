def make(lis, n, en, num):
    for i in lis:
        if n == en and type(i) == int:
            num += 1
        if type(i) != int:
            num = make(i, n + 1, en, num)
    return num


lis = eval(input())
ceng = eval(input())
num = make(lis, 1, ceng, 0)
print(num)
