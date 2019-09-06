string = input()
char = 0
num = 0
null = 0
other = 0
for i in string:
    if i.isalpha():
        char += 1
    elif i.isspace():
        null += 1
    elif i.isdecimal():
        num += 1
    else:
        other += 1
print("{} {} {} {}".format(char, null, num, other))