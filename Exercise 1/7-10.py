import math

ls = input()
ls = ls.split()
money = int(ls[0])
year = int(ls[1])
rate = float(ls[2])
print("interest={:.2f}".format(money * math.pow((1 + rate), year) - money))
