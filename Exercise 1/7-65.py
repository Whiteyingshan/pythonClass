l = eval(input())
r = eval(input())
num = 0
for i in range(l, r + 1):
    if i % 3 == 0 or i % 5 == 0:
        num += i
print(num)
