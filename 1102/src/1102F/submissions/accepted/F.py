import sys
for line in sys.stdin.read().splitlines()[1::]:
    num = [int(i) for i in line.split()]
    ans = 0
    for i in range(0,len(num)):
        for j in range(0,len(num)):
            if num[i]>num[j] and i<j:
                ans+=1
    print(ans)