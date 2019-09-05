year=eval(input())
if year%100!=0 and year%4==0 or year%400==0:
    print("{}是闰年".format(year))
else:
    print("{}不是闰年".format(year))