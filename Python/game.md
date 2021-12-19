---
title: 剪刀 石頭 布
tags: Python
---

## 剪刀 石頭 布 
:::info
我出的拳：[0]剪刀 [1]石頭 [2]布
電腦出拳：[0]剪刀 [1]石頭 [2]布
[0]Scissors [1]Rock [2]Cloth
:::

<!---
:::success
IMD2021A
https://judge.ntub.tw/public/
https://judge.ntub.tw/public/problems/174/text
:::
--->

### 輸入
:::warning
我出的拳：[0]剪刀 [1]石頭 [2]布 和 電腦出拳：[0]剪刀 [1]石頭 [2]布
:::

### 輸出
:::success
平手, 我贏了, 我輸了
Tie, I won, I lost
:::

### 範例輸入輸出
範例輸入 I
[0]剪刀 [1]石頭 [2]布
1.in
```shell=
0 0
0 1
0 2
```
範例輸出 I
```shell=
Tie
I lost
I won
```
範例輸入 II
[0]剪刀 [1]石頭 [2]布
2.in
```shell=
1 0
1 1
1 2
2 0
2 1
2 2
```

範例輸出 II
```shell=
I won
Tie
I lost
I lost
I won
Tie
```


```python=
# game.py
# [0]剪刀 [1]石頭 [2]布
import sys

lines=sys.stdin.read().splitlines()
while len(lines)>0:
    a,b=[int(f) for f in lines.pop(0).split()]
    if a==0:
        if b == 0:
            print("Tie")
        elif b == 1:
            print("I lost")
        else:
            print("I won")
    elif a==1:
        if b == 1:
            print("Tie")
        elif b == 2:
            print("I lost")
        else:
            print("I won")
    else:
        if b == 2:
            print("Tie")
        elif b == 0:
            print("I lost")
        else:
            print("I won")
```
```shell=
python game.py < 1.in
```

```python=
# [0]剪刀 [1]石頭 [2]布
import sys
for input in sys.stdin.read().splitlines():
    a,b = input.strip().split()
    if a == b:
        print('Tie')   
    elif a == '0' and b == '1':
        print('I lost')
    elif a == '0' and b == '2':
        print('I won')
    elif a == '1' and b == '0':
        print('I won')
    elif a == '1' and b == '2':
        print('I lost')    
    elif a == '2' and b == '0':
        print('I lost')
    elif a == '2' and b == '1':
        print('I won')
```

```python=
# [0]剪刀 [1]石頭 [2]布
try:
    while True:
        a,b=map(int,input().split())
        if a==b:
            print("Tie")
        elif a==0 and b==2:
            print("I won")
        elif a==1 and b==0:
            print("I won")
        elif a==2 and b==1:
            print("I won")
        else:
            print("I lost")
except:
    pass
```

```python=
#IMD2021A
#Problem 剪刀石頭布
#[0]剪刀 [1]石頭 [2]布
#while True:
while 1:
    try:
        a,b=map(int,input().split())
        if a==b:
            print("Tie")
        elif (a==0 and b==1) or (a==1 and b==2) or (a==2 and b==0):
            print("I lost")
        elif (a==0 and b==2) or (a==1 and b==0) or (a==2 and b==1) :
            print("I won")
    except:
        break
```

```python=
# [0]剪刀 [1]石頭 [2]布
from sys import stdin
n = stdin.readline()

while n :
    a,b = map(int,n.split())
    if a == b:
        print("Tie")
    elif (a==0 and b==1) or (a==1 and b==2) or (a==2 and b==0):
        print("I lost")
    else:
        print("I won")
    n = stdin.readline()
```


```python=
# [0]剪刀 [1]石頭 [2]布
while True:   
    try:
        a,b=list(map(int,input().split('')))
        #0,2 1,0 2,1
        if [a,b] in [[0,0],[1,1],[2,2]]:
            print('Tie')
        elif [a,b] in [[0,2],[1,0],[2,1]]:
            print('I won')
        else:
            print('I lost')
    except:
        break
```

```python=
from sys import stdin

di = {(0,0):'Tie', (0,1):'I lost', (0,2):'I won',
      (1,0):'I won', (1,1):'Tie', (1,2):'I lost',
      (2,0):'I lost', (2,1):'I won', (2,2):'Tie'}
for s in stdin:
    a = tuple(map(int, s.split()))
    print(di[a])
```


:::spoiler 特殊解法

```python=
import sys

def game(a,b):
    if a == b:
        return("Tie")
    elif a == (b + 1) % 3:
        return("I won")
    else:
        return("I lost")

lines = sys.stdin.read().splitlines()
for line in lines:
    a, b = [ int(x) for x in line.split() ]
    print(game(a,b))
```

```python=
import random

key_word = ['剪刀', '石頭', '布']

user = int(input('[0]剪刀, [1]石頭, [2]布:'))
rand_num = random.randint(0, 2)

print('你出了: ', key_word[user])
print('電腦出了: ', key_word[rand_num])

if rand_num == (int(user)-1)%3:
  print('I won')
elif rand_num == (int(user)+1)%3:
  print('I lost')
else:
  print('Tie')
```
:::

<div id="moon"></div>

<style>
#moon {
  width: 80px;
  height: 80px;
  page-break-after: always /*在標籤後換頁*/
}
</style>

---
