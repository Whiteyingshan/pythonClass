import random

x, n = map(int, input().split())
random.seed(x)
ans = 0
for i in range(n):
    lis = [random.randint(1, 365) for _ in range(23)]
    lis_set = set(lis)
    num = 0
    for i in lis_set:
        if lis.count(i) != 1:
            ans += 1
            break
print("rate={:.2f}".format(ans / n))
