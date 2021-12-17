def cmp(s1, s2):
    cnt = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            cnt += 1
    return cnt <= 1
 
T = int(input())
for _ in range(T):
    s = input()
    if len(s) == 5:
        print(3)
    else:
        if cmp("one", s):
            print(1)
        if cmp("two", s):
            print(2)