import math

x = eval(input())
if abs(x) < 1:
    print("f({:.3f})={:.3f}".format(x, math.sqrt(2 - 2 * x)))
elif x >= 1:
    print("f({:.3f})={:.3f}".format(x, (math.cos(x) + pow(x,2)) / (2.5 + abs(x + math.log(100,math.e)))))
else:
    print("f({:.3f})={:.3f}".format(x, math.pow(math.e,x)))
