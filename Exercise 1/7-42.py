s = input()
l = eval(input())
r = eval(input())
if l-1>=0 and r<=len(s):
    print("{}".format(s[l - 1:r]))
else:
    print("没子串！")
