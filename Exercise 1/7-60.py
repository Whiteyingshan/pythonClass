lis1 = input().split()
lis2 = input().split()
dic = dict()
for i in range(len(lis1)):
    dic[lis1[i]] = lis2[i]
lis = sorted(dic.items())
print(lis)
