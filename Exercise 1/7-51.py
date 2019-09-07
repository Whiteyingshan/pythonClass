import math

a, b = map(int, input().split(','))
print("GCD:{}, LCM:{}".format(math.gcd(a, b), a * b // math.gcd(a, b)))
