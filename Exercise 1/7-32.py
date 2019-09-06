dic1 = eval(input())
dic2 = eval(input())
for key in dic1:
    if dic2.__contains__(key):
        dic2[key] += dic1[key]
    else:
        dic2[key] = dic1[key]
dictor1 = {}
dictor2 = {}
for k in dic2:
    if type(k) == int:
        dictor1[k] = dic2[k]
    else:
        dictor2[k] = dic2[k]
print("{", end='')
length = len(dictor1) + len(dictor2)
c = 0
for k in sorted(dictor1):
    if c != length-1:
        print("{}:{},".format(k, dictor1[k]), end='')
    else:
        print("{}:{}".format(k, dictor1[k]), end='')
    c += 1
for k in sorted(dictor2):
    if c != length-1:
        print("\"{}\":{},".format(k, dictor2[k]), end='')
    else:
        print("\"{}\":{}".format(k, dictor2[k]), end='')
    c += 1
print("}")
