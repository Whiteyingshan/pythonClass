import math

n = eval(input())
if abs(n) >= 300:
    print("f({:.3f})={:.3f}".format(n, -1))
else:
    print("f({:.3f})={:.3f}".format(n, (math.pow(n, 3) / (math.log10(math.fabs(n) + 2.6)))))
