n = eval(input())
num = 1
ans = 0
for i in range(1, n + 1):
    num *= i
    ans += num
print(ans)
