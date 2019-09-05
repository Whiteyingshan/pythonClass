n = eval(input())
ans = 1
for i in range(1, n + 1):
    if not i%2 :
        ans *= i
print(ans)
