import math

x = eval(input())
print("f({:.3f})=".format(x), end='')
if abs(x) >= 300:
    print("{:.3f}".format(-1))
elif abs(x) < 300:
    print("{:.3f}".format(x ** 3 / (math.log10(math.fabs(x) + 2.6))))
