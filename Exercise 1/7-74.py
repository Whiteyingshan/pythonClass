num = 0
ans = 0
noNum = 0
while True:
    n = eval(input())
    if n < 0:
        break
    if n < 60:
        noNum += 1
    num += 1
    ans += n
if num:
    print("平均分={:.2f},不及格人数={}".format(ans / num, noNum))
else:
    print("没有学生")
