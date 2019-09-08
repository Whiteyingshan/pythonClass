s = dict()
while True:
    lis = input().split()
    if lis and lis[0] == "!!!!!":
        break
    for i in lis:
        if s.__contains__(i):
            s[i] += 1
        else:
            s[i] = 1
num = 0
print(len(s))
for i in sorted(s):
    if num >= 10:
        break
    print(i)
    num += 1
