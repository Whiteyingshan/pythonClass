lens = eval(input())
for i in range(1, pow(10, lens)):
    t = i
    ans = 0
    while t != 0:
        ans += pow(t % 10, 5)
        t //= 10
    if ans == i:
        print(i)
