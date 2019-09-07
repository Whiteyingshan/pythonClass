lis = input()
lis = lis.split()
lis = [float(i) for i in lis]
for i in range(len(lis)):
    if lis[i] < 5000:
        print("{}".format(lis[i] * 1.5),end='')
    else:
        print("{:.0f}".format(lis[i]),end='')
    if i != len(lis) - 1:
        print(end=' ')
