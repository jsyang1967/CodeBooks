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
我出的拳：[0]剪刀 [1]石頭 [2]布 和 

電腦出拳：[0]剪刀 [1]石頭 [2]布
:::

### 輸出
:::success
平手, 我贏了, 我輸了
Tie, I won, I lost
:::

### 範例輸入輸出
範例輸入 I ：我跟電腦猜了3次拳，如果我都出剪刀的話勝負結果是？

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
---
範例輸入 II ：我跟電腦猜了6次拳，如果我出石頭或布的話勝負結果是？

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

---
## 程式範例
### 方法一
```python=
# game.py
# [0]剪刀 [1]石頭 [2]布
import sys
# 讀取多行後再印出。可以import sys 使用下面的程式來執行；
# 讀取多行也可以使用 readlines()，但lines每行後面會帶有\n，
# 用read()讀取再呼叫splitlines()的話可以去掉後面的換行符
lines=sys.stdin.read().splitlines()

# len(參數)：算參數長度
while len(lines)>0:
    a,b=[int(f) for f in lines.pop(0).split()]
    #這段 int(f) for f in lines.pop(0).split() 等同於下面的for
    #for f in lines.pop(0).split():
    #    int(f)
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

### 方法二
```python=
# [0]剪刀 [1]石頭 [2]布
import sys
for input in sys.stdin.read().splitlines():
    #strip()去除空格 split()分割字串
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
### 方法三 map用法；列出「我」贏狀況，其他狀況就輸了
```python=
# [0]剪刀 [1]石頭 [2]布 
# 雙方一樣則平手，
# 如果「我」出剪刀，「電腦」出布，「我」就贏
# 如果「我」出石頭，「電腦」出剪刀，「我」就贏
# 如果「我」出布，「電腦」出石頭，「我」就贏
# 其餘狀況都「我」輸
try:
    while True:
        #map(函數,內容)
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
### 方法四 map 用法；詳細列出可能結果
```python=
#IMD2021A
#Problem 剪刀石頭布
#[0]剪刀 [1]石頭 [2]布
#while True: 
#while 1:  的速度比  while True:快，但二個都可以用
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
### 方法五 map 用法；沒有平手、沒有輸的話，就贏了
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

### 方法六 list 用法
```python=
# [0]剪刀 [1]石頭 [2]布 
while True:   
    try:
        #list=[] ：list列表可存內容
        a,b=list(map(int,input().split('')))
        #例：[0,2] [1,0] [2,1]
        if [a,b] in [[0,0],[1,1],[2,2]]:
            print('Tie')
        elif [a,b] in [[0,2],[1,0],[2,1]]:
            print('I won')
        else:
            print('I lost')
    except:
        break
```

### 方法七 Tuple用法
```python=
# [0]剪刀 [1]石頭 [2]布  
from sys import stdin

di = {(0,0):'Tie', (0,1):'I lost', (0,2):'I won',
      (1,0):'I won', (1,1):'Tie', (1,2):'I lost',
      (2,0):'I lost', (2,1):'I won', (2,2):'Tie'}
for s in stdin:
    a = tuple(map(int, s.split()))
    print(di[a])
```

### 特殊解法
:::spoiler 特殊解法

### 方法八 函數宣告；%餘數運算
```python=
# [0]剪刀 [1]石頭 [2]布  
import sys

def game(a,b):
    if a == b:
        return("Tie")
    elif a == (b + 1) % 3:  # % 取餘數
        return("I won") # (0,2) (1,0) (2,1) 這三個狀況會贏，可代入看看喔/
    else:
        return("I lost")

lines = sys.stdin.read().splitlines()
for line in lines:
    a, b = [ int(x) for x in line.split() ]
    print(game(a,b))
```

### 方法九 Random 隨機出拳
```python=
# [0]剪刀 [1]石頭 [2]布
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

## 剪刀 石頭 布(練習) 
可參考上方程式範例方法一~九

:::info
玩家1出的拳：[Y]剪刀 [O]石頭 [X]布

玩家2出的拳：[Y]剪刀 [O]石頭 [X]布
[Y]Scissors [O]Rock [X]Cloth
:::


### 輸入
:::warning
玩家1出的拳：[Y]剪刀 [O]石頭 [X]布 和 
玩家2出的拳：[Y]剪刀 [O]石頭 [X]布
:::

### 輸出
:::success
平手:0，玩家1贏了:1，玩家2贏了:2。輸出為0,1,2。
:::

### 範例輸入輸出
範例輸入 I
[Y]剪刀 [O]石頭 [X]布
1.in
```shell=
Y Y
Y O
Y X
```
範例輸出 I
```shell=
0
2
1
```
---
範例輸入 II
[Y]剪刀 [O]石頭 [X]布
2.in
```shell=
O Y
O O
O X
X Y
X O
X X
```

範例輸出 II
```shell=
1
0
2
2
1
0
```
