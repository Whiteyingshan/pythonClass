def Freq(line):
    dic = dict()
    for i in line:
        if dic.__contains__(i):
            dic[i] += 1
        else:
            dic.update({i: 1})
    n = len(dic)
    num = 0
    print(n)
    for i in sorted(dic):
        num += 1
        if num == n:
            print("{} = {}".format(i, dic[i]), end='')
        else:
            print("{} = {}".format(i, dic[i]))


# 请在这里填写答案
line = input()
Freq(line)
