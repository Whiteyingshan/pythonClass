ls = input()
ls = ls.split()
ls = list(map(float, ls))
ans = 0
for i in ls:
    ans += i
print(ls.__len__())
print("{:.3f}".format(ans))
