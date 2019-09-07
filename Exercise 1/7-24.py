n=eval(input())
for i in range(n):
    lis=input().split()
    first=True
    delNum=input()
    for i in lis:
        if i != delNum:
            if first:
                print(i,end='')
                first=False
            else:
                print(" {}".format(i),end='')
    print()