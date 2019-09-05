def isPrime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def primeSum(x, y):
    ans = 0
    for i in range(x, y + 1):
        if isPrime(i):
            ans += i
    return ans

# 请在这里填写答案
x, y = map(int, input().split())
print(primeSum(x, y))
