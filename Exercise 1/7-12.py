string=input()
num=0
ch=0
for i in string:
    if i.isdigit():
        num+=1
    elif i.islower():
        ch+=1
print("共有{}个数字，{}个小写字符".format(num,ch))