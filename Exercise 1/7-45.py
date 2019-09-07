try:
    st=input()
    if st[0] == '$':
        money=int(st[1:])*7
        print("￥{:.2f}".format(money))
    elif st[0] == '￥':
        money=int(st[1:])/7
        print("${:.2f}".format(money))
    else:
        print("输入格式错误")
except:
    print("输入格式错误")