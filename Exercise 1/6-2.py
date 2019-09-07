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


# 请在这里填写答案
n = int(input())
for i in range(n):
    p = readPoint()
    print('Point = {}, type = {}, distance = {:.3f}'.format(p, type(p), distance(p)))
