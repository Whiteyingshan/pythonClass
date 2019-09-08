def make(lis, n):
    ans = 0
    for i in lis:
        if type(i) == int:
            ans += i * n
        else:
            ans += make(i, n + 1)
    return ans


lis = eval(input())
ans = make(lis, 1)
print(ans)
