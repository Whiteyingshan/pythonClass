ans = 1
while True:
    if ans % 5 == 1 and ans % 6 == 5 and ans % 7 == 4 and ans % 11 == 10:
        break
    ans += 1
print(ans)
