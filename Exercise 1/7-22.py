n = eval(input())
true = 0
false = 0
while n:
    ls = []
    ls = input()
    ls=ls.split()
    if len(ls)!=len(set(ls)):
        true+=1
    else:
        false+=1
    n-=1
print("True={}, False={}".format(true, false))
