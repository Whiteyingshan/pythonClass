try:
    lis = eval(input())
    if type(lis) == int or type(lis) == float or type(lis) == complex:
        print("yes")
    else:
        print("no")
except:
    print("no")