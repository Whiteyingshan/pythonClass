import random
from random import seed


def generatePoints(n):  # 产生n个2维坐标点放入列表并返回该列表
    lis = []
    for i in range(n):
        x, y = random.randint(0, 10), random.randint(0, 10)
        lis.append((x, y))
    return lis


def createPointDict(pList):  # 将pList中的节点加入字典并统计出现次数，然后返回字典
    dic = dict()
    for i in pList:
        if dic.__contains__(i):
            dic[i] += 1
        else:
            dic[i] = 1
    return dic


def doQuery(pDict, p):  # 在pDict中查询p，如果查到则输出该点及其出现次数，否则输出'Not Found'。
    if pDict.__contains__(p):
        print("{} = {}".format(p, pDict[p]))
    else:
        print("Not Found")


# 请在这里填写答案


n = int(input())
seed(int(input()))
pList = generatePoints(n)
pDict = createPointDict(pList)
for i in range(3):  # 查询3次
    x, y = [int(e) for e in input().split(',')]
    doQuery(pDict, (x, y))
