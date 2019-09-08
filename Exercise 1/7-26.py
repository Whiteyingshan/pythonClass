n = eval(input())
avg = 0
i = 1
Total = 0
OK = 0
Error = 0
while i <= n:
    p = ""
    try:
        p = input()
        x = eval(p)
        avg += x
        OK += 1
    except EOFError:
        print("end of files")
        break
    except:
        Error += 1
        print('line {} error for input "{}"'.format(i, p))
    i += 1
    Total += 1
print("Total: {}".format(Total))
print("OK: {}".format(OK))
print("Error: {}".format(Error))
print("avg grade = {:.2f}".format(avg / OK))
