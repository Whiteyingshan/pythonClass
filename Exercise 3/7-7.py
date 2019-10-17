a, b = map(int, input().split(','))
num = 1
ans = 0
while a:
    ans += a % 10 * num
    num *= b
    a //= 10
print(ans)
