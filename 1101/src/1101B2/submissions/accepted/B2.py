t = int(input())
for _ in range(t):
    y = int(input())
    if ((y%4==0) and (y%100!=0)) or (y%400==0):
        print("a leap year")
    else:
        print("a normal year")