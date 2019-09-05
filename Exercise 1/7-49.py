x=eval(input())
if x<3:
    print("f({:.2f})={:.2f}".format(x,1.2))
elif x==3:
    print("f({:.2f})={:.2f}".format(x,10))
elif x>3:
    print("f({:.2f})={:.2f}".format(x,2*x+1))