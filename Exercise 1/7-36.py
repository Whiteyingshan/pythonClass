lis = input()
k = eval(input())
for i in range(len(lis)):
    if lis[i].islower():
        print(chr((ord(lis[i]) + k - ord('a')) % 26 + ord('a')), end='')
    elif lis[i].isupper():
        print(chr((ord(lis[i]) + k - ord('A')) % 26 + ord('A')), end='')
    else:
        print(lis[i], end='')
