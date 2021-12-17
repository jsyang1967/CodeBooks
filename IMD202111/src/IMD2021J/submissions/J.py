def lis(arr):
	n = len(arr)
	lis = [1]*n
	for i in range (1, n):
		for j in range(0, i):
			if arr[i] > arr[j] and lis[i]< lis[j] + 1 :
				lis[i] = lis[j]+1
	maximum = 0
	for i in range(n):
		maximum = max(maximum, lis[i])
	return maximum

import sys
for line in sys.stdin.read().splitlines():
    arr=[int(num) for num in line.split()]     
    #arr = [10, 22, 9, 33, 21, 50, 41, 60]
    print(lis(arr))
