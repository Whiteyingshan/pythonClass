n = eval(input())
for i in range(n):
    num = eval(input())
    print("{} = {}*10 + {}*5 + {}*1".format(num, num // 10, (num - num // 10 * 10) // 5, num % 5))
