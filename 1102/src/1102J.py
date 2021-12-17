import sys
import time

# start_time = time.time()

aa = map(int, sys.stdin.read().splitlines()[1].split())

for n in aa:
    while (n % 2 == 0):
        n = n / 2
    while n % 3 == 0:
        n = n / 3
    while n % 5 == 0:
        n = n / 5
    if n != 1:
        print(False)
    else:
        print(True)

# print("--- %s seconds ---" % (time.time() - start_time))