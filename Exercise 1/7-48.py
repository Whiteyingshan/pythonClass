while True:
    try:
        ls = input()
        ls = ls.split()
        if ls:
            print(len(ls))
    except:
        break
