def isPrime(num):
    try:
        n=int(num)
        for i in range(2, n):
            if not n % i:
                return False
        return True
    except:
        return False


# 请在这里填写答案
num = input()
if isPrime(num):
    print('yes')
else:
    print('no')
