x=input()
if x[0] is 'R':
    print("${:.2f}".format(int(x[1:])/6))
else:
    print("R{:.2f}".format(int(x[1:])*6))