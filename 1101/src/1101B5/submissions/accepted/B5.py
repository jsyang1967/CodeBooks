import sys
for line in sys.stdin.readlines():
    y = int(line)
    if ((y%4==0) and (y%100!=0)) or (y%400==0):
        print("a leap year")
    else:
        print("a normal year")