try:
    lis = input()
    n = eval(input())
    print("{}".format(lis[n]))
except NameError:
    print("下标要整数")
except IndexError:
    print("下标越界")
