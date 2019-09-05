s = input()
s = s.split()
s = list(map(int, s))
s.sort()
if s[2] >= s[0] + s[1]:
    print("no")
else:
    print("yes")
