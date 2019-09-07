def giveChange(money):  # money代表要找的钱，为整数。该函数经过计算，然后按照格式"要找的钱 = x*10 + y*5 + z*1"直接输出。
    num10, num5, num1 = 0, 0, 0
    Nmoney = money
    num10 = Nmoney // 10
    Nmoney %= 10
    num5 = Nmoney // 5
    Nmoney %= 5
    num1 = Nmoney
    print("{} = {}*10 + {}*5 + {}*1".format(money, num10, num5, num1))


# 请在这里填写答案
n = int(input())
for i in range(n):
    giveChange(int(input()))
