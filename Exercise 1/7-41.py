import math  #导入math库
a=eval(input())
b=eval(input())
c=eval(input())
s=(a+b+c)/2
print("area={1:.2f};perimeter={0:.2f}".format(a+b+c,math.sqrt(s*(s-a)*(s-b)*(s-c))))