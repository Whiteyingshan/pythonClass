n = eval(input())
i = 0
ans = 0
p = ""
try:
    while i < n:
        p = input()
        ans += eval(p)
        i += 1
except:
    print('Error for data "{}"! Break'.format(p))
else:
    print("All OK")
finally:
    print("Process Completed")
if i == n:
    print("avg grade = {:.2f}".format(ans / n))
