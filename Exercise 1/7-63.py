import math

try:
    m, n = map(int, input().split())
    if n < 0 or m < 0:
        print("不能负数")
    else:
        print(f"result={math.factorial(n) / (math.factorial(m) * math.factorial(n - m)):.2f}")
except:
    print("请输入数值")
