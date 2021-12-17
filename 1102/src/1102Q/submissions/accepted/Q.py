while True:
    try:
        n = int(input())
        a = list(map(int, input().split()))
        a.sort(reverse=True)
        ans = 0
        while (len(a) > 1):
            n1 = a.pop()
            n2 = a.pop()
            a.append(n1 + n2)
            a.sort(reverse=True)
            ans += (n1 + n2)
 
        print(ans)
    except:
        break