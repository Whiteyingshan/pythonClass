n=eval(input())
for i in range(n):
    m=eval(input())
    x=m
    a=m//10
    m%=10
    b=m//5
    m%=5
    print("{0} = {1}*10 + {2}*5 + {3}*1".format(x,a,b,m))