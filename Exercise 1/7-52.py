import random
from random import seed

lis = []
for i in range(ord('a'), ord('z') + 1):
    lis.append(chr(i))
for i in range(ord('A'), ord('Z') + 1):
    lis.append(chr(i))
for i in range(ord('0'), ord('9') + 1):
    lis.append(chr(i))
x = eval(input())
seed(x)
n = eval(input())
m = eval(input())
for i in range(n):
    num = []
    for j in range(m):
        num.append(lis[random.randint(0, len(lis)-1)])
    print(''.join(num))
