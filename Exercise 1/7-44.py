n = eval(input())
sup = dict()
for i in range(n):
    s = input()
    sup[s] = len(s)
for i in sorted(sup, key=lambda m: sup[m]):
    print("({}, '{}')".format(sup[i], i))
