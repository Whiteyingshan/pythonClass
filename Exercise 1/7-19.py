import random
from random import seed

n, m = map(int, input().split())
seed(m)
num = 0
while True:
    x = random.randint(1,10)
    num += 1
    if x == n:
        break
print("{} times to got it".format(num))
