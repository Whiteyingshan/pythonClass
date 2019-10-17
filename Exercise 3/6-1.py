def CountDigit(number, digit):
    n = abs(number)
    num = 0
    while n:
        if n % 10 == digit:
            num += 1
        n = n // 10
    return num


# /* 请在这里填写答案 */

number, digit = input().split()
number = int(number)
digit = int(digit)
count = CountDigit(number, digit)
print("Number of digit 2 in " + str(number) + ":", count)
