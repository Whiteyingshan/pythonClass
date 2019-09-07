n = eval(input())
ls = []
for i in range(n):
    ls = input()
    ls = ls.split()
    if ls[0] is 'M':
        print("{:.2f}".format(float(ls[1]) / 1.09))
    else:
        print("{:.2f}".format(float(ls[1]) * 1.09))