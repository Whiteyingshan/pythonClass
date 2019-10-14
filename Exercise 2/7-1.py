n = input()
money = eval(n[1:])
freon = n[0]
if freon == 'R':
    print("${:.2f}".format(money / 6))
else:
    print("R{:.2f}".format(money * 6))
