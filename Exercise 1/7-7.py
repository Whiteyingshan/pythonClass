ls1=[]
ls1=input()
ls1.split(",")
ls2=[]
for i in ls1:
    if i not in ls2:
        ls2.append(i)
for i in ls2:
    if i != '[' and i!= ']' and i != ',':
        print(i,end=' ')