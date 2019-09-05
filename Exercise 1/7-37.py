try:
    n = eval(input())
    if n <= -2:
        print("y={:.2f}".format(-2 * n - 1))
    elif -2 < n <= 1:
        print("y={:.2f}".format(3))
    else:
        print("y={:.2f}".format(2 * n + 1))
except:
    print("Input Error!")
