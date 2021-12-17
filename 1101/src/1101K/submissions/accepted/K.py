import sys
n = int(sys.stdin.readline())

def solve():
    string1 ="_" + sys.stdin.readline().replace("\n","")
    string2 ="=" + sys.stdin.readline().replace("\n","")
    n1 = len(string1)
    n2 = len(string2)
    dp = [[0 for t1 in range(n1)] for t2 in range(n2)]
    for i in range(1,n2):
        for j in range(1,n1):
            dp[i][j] = dp[i-1][j-1]+1 if string1[j] == string2[i] else max(dp[i-1][j],dp[i][j-1])
    print(dp[n2-1][n1-1])

for i in range(n):
    solve()