string=input()
ch=input()
x=string.find(ch)
if x is -1:
    print("can't find letter {}".format(ch))
else:
    print("index={}".format(x+1))