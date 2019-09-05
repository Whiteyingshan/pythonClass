ls = input()
ls = ls.split()
ls = list(map(float, ls))
ans = 0
num = 0
for i in ls:
    ans += i
    num += 1
print(num)
print("{:.3f}".format(ans))
