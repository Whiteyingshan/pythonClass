a = eval(input())
b = set(a)
b = list(b)
b.sort(key=a.index)
for i in range(len(b)):
    if i == len(b) - 1:
        print(b[i])
    else:
        print(b[i], end=' ')
