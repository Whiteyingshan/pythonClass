def printYanghui(n):  # 打印n行杨辉三角型
    lis = [[0 for i in range(20)] for j in range(20)]
    for i in range(n):
        for j in range(i + 1):
            if j == 0 or j == i:
                lis[i][j] = 1
            else:
                lis[i][j] = lis[i - 1][j] + lis[i - 1][j - 1]
    for i in range(n - 1, -1, -1):
        for j in range(i):
            print(end=' ')
        for j in range(n - i):
            print(lis[n - i -1][j],end=' ')
        if i != 0:
            print()


# 请在这里填写答案
n = int(input())
printYanghui(n)
