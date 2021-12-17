lst = list(map(int, input().split()))
lst.sort()
prnt = ''
x = str(input())
x = list(x)

for i in x:
    if i == 'A': prnt += str(lst[0])
    elif i == 'B': prnt += str(lst[1])
    else:prnt += str(lst[2])
    prnt += ' '
print(prnt)