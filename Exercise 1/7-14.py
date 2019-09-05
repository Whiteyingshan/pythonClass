n=eval(input())
for i in range(n):
    try:
        m=eval(input())
        print("{:.2f}".format(m))
    except NameError:
        print("NameError")
    except ZeroDivisionError:
        print("ZeroDivisionError")
    except SyntaxError:
        print("SyntaxError")