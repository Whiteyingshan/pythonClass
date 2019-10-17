lis = list()
string = input()
for i in string:
    if i.isalpha() and i.lower() not in lis and i.upper() not in lis and i is not ' ':
        lis.append(i)
if len(lis) >= 10:
    for i in range(10):
        print(lis[i], end='')
else:
    print("not found")
