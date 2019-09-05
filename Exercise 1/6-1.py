import math
def get_rList(n):
    ls=[]
    for i in range(n):
        x=eval(input())
        ls.append(x)
    return ls
def getCircleArea(e):
    return e*e*math.pi