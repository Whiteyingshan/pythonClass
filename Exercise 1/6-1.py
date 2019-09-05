import math


def get_rList(n):
    ls = []
    for i in range(n):
        x = eval(input())
        ls.append(x)
    return ls


def getCircleArea(e):
    return e * e * math.pi


# 请在这里填写答案
n = int(input())
rList = get_rList(n)
for e in rList:
    print('{:10.3f}'.format(getCircleArea(e)))
print(type(rList))
