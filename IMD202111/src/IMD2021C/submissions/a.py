import sys

for line in sys.stdin.read().splitlines():
    nums=[int(num) for num in line.split()]       
    print(nums[0]*24+nums[1]*14+nums[2]*6)