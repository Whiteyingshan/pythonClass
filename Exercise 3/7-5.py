string = input().strip()
ch = input().strip()
print("result: ", end='')
for i in string:
    if i not in [ch.upper(), ch.lower()]:
        print(i, end='')
