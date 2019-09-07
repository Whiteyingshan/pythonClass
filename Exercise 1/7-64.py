n = eval(input())
if n <= 1:
    print("{} is not prime".format(n))
else:
    for i in range(2, n):
        if n % i == 0:
            print("{} is not prime".format(n))
            break
    else:
        print("{} is prime".format(n))
