string = input()
s = []
for i in string:
    if i.isalpha() and i not in s and  i.upper() not in s and i.lower() not in s:
        s.append(i)
    if len(s) == 10:
        break
if len(s) == 10:
    for i in s:
        print(i, end='')
else:
    print("not found")
