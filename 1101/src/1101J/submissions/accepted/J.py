import sys

class Node(object):
	def __init__(self, value):
		self.value = value 
		self.next = None

def create_linkList(n):
	head = Node(1)
	pre = head
	for i in range(2, n+1):
		newNode = Node(i)
		pre.next= newNode
		pre = newNode
	pre.next = head
	return head

for line in sys.stdin.read().splitlines():
    # splitlines 會去除不同OS的換行符號
    nums = [int(num) for num in line.split()]
    # nums = map(int, line.split())
    n = nums[0] #總的個數
    m = nums[1] #數的數目
    if m == 1: #如果是1的话，特殊處理，直接輸出
        print (n)  
    else:
        head = create_linkList(n)
        pre = None
        cur = head
        while cur.next != cur: #终止條件是節點的下一个節點指向本身
            for i in range(m-1):
                pre =  cur
                cur = cur.next
            #print (cur.value)
            pre.next = cur.next
            cur.next = None
            cur = pre.next
        print (cur.value)