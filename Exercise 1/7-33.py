a = eval(input())
op = input()
b = eval(input())
if op == '+':
    print("{:.2f}".format(a + b))
elif op == '-':
    print("{:.2f}".format(a - b))
elif op == '*':
    print("{:.2f}".format(a * b))
elif op == '/':
    try:
        print("{:.2f}".format(a / b))
    except:
        print("divided by zero")
