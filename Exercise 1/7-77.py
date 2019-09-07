try:
    n=eval(input())
    num=0
    for i in range(n):
        num+=eval(input())
    print("正确\navg={:.2f}".format(num/n))
except ZeroDivisionError:
    print("除0错误，n不能等0")
except NameError:
    print("数值错误")
finally:
    print("程序结束")