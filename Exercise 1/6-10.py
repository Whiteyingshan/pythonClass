def change(x):
    if x[0] is '$':
        dollar = int(x[1:])
        rmb = dollar * 6.709
        print("{}美元 = {:.2f}人民币".format(dollar, rmb))
    else:
        rmb = int(x[1:])
        dollar = rmb / 6.709
        print("{}人民币 = {:.2f}美元".format(rmb, dollar))


# 请在这里填写答案
x = input()
change(x)
