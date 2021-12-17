import sys

for line in sys.stdin.read().splitlines():
    nums=[int(num) for num in line.split()]       
    print(nums[0]*4+nums[1]*6)