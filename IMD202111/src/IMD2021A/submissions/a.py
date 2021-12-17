import sys

for line in sys.stdin.read().splitlines():
    nums=[int(num) for num in line.split()]       
    print(nums[0]*56+nums[1]*24+nums[2]*14+nums[3]*6+nums[4]*2)