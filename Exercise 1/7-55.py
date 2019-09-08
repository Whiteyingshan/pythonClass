line = eval(input())
V = 0
E = 0
Len = 0
for i in range(line):
    lis = eval(input())
    for j in lis:
        V += 1
        ma = eval(str(lis[j]))
        for k in ma:
            E += 1
            Len += ma[k]
print("{} {} {}".format(V, E, Len))
