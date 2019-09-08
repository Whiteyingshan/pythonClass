s = dict()
while True:
    lis = input()
    if lis and lis == "!!!!!":
        break
    lis = lis.replace('!', '')
    lis = lis.replace('.', '')
    lis = lis.replace(',', '')
    lis = lis.replace(':', '')
    lis = lis.replace('?', '')
    lis = lis.replace('*', '')
    lis = lis.lower()
    lis = lis.split()
    for i in lis:
        if s.__contains__(i):
            s[i] += 1
        else:
            s[i] = 1
num = 0
print(len(s))
for i in sorted(s.items(), key=lambda s: (-s[1], s[0])):
    if num >= 10:
        break
    mo = list(i)
    print("{}={}".format(mo[0], mo[1]))
    num += 1
