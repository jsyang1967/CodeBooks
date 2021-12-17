import sys
for i in sys.stdin:
    N, M = map(int, i.split())
    # 城市編號從 1 開始
    G = [list() for i in range(N+1)]
    for i in range(M):
        a, b = map(int, sys.stdin.readline().split())
        G[a].append(b)
 
    a, b = map(int, sys.stdin.readline().split())
    q = [a]
    ex = [0 for i in range(N+1)]
    while (q):
        now = q.pop(0)
        ex[now] = 1
        for nxt in G[now]:
            if (ex[nxt] == 0):
                ex[nxt] = 1
                q.append(nxt)
 
    if (ex[b]):
        print("Yes")
    else:
        print("No")