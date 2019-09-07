import math


def readPoint():
    point = input()
    point = point.split(',')
    for i in range(len(point)):
        if not point[i]:
            point.append(i)
    point = tuple(map(int, point))
    return point


def distance(point):
    return math.sqrt(point[0] * point[0] + point[1] * point[1] + point[2] * point[2])


def ClassifyPoints(points, r):  # 根据r将points中的点分成两类放入两个列表，距离小于r与大于等于r。然后将两个列表以元组的形式返回
    a = []
    b = []
    for i in points:
        if distance(i) < r:
            a.append(i)
        else:
            b.append(i)
    return a, b


def avgDistance(pointList):  # 计算列表pointList中的所有点到原点的平均距离，可利用distance(p)函数
    avg = 0
    for i in pointList:
        avg += distance(i)
    return avg / len(pointList)


def printPointsTuple(psTuple, r):  # 将元组psTuple中的数据按照输出样例格式输出。输出顺序由psTuple中点列表的顺序决定。
    dis1 = psTuple[0]
    dis2 = psTuple[1]
    print("distance < {}, avgDistance = {:.3f}, points = {}".format(r, avgDistance(dis1), dis1))
    print("distance >= {}, avgDistance = {:.3f}, points = {}".format(r, avgDistance(dis2), dis2))


# 请在这里填写答案
n = int(input())
r = int(input())
points = []
for i in range(n):
    p = readPoint()
    points.append(p)
    print('Point = {}, type = {}, distance = {:.3f}'.format(p, type(p), distance(p)))

pointsTuple = ClassifyPoints(points, r)
print("pointsTuple = {}".format(pointsTuple))
printPointsTuple(pointsTuple, r)
