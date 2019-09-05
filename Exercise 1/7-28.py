li=input()
li=li.split()
li2=li[::-1]
for i in li2:
    print(i,end='')
print()
print(li)
for i in range(len(li2)):
    if i==len(li2)-1:
        print(li2[i])
    else:
        print(li2[i],end=' ')
