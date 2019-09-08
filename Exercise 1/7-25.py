n = eval(input())
num = n
Nonthing = True
avg = 0
i = 0
while i < num:
    p = ""
    try:
        p = input()
        a = eval(p)
        avg += a
    except:
        print("Error for data {}! Reinput".format(p))
        Nonthing = False
        num += 1
    i += 1
if Nonthing:
    print("All OK")
print("avg grade = {:.2f}".format(avg / n))
