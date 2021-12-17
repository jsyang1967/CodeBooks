def ip_checksum(ip_header,size):
    cksum = 0
    pointer = 0
    if size % 2 != 0:
        ip_header += '0'
        size = len(ip_header)
    while size > 1:
        cksum += int(ip_header[pointer] + ip_header[pointer + 1],16)
        size -= 2
        pointer += 2

    cksum = (cksum >> 16) + (cksum & 0xffff)
    cksum += (cksum >> 16)
    return (~cksum) & 0xFFFF
    #return (cksum) & 0xFFFF
#data = "45 00 00 30 cc 61 40 00 40 06 00 00 0a 05 04 6b 0a 08 09 ed"
#Ans 4c 02

#data = "45 00 00 47 73 88 40 00 40 06 00 00 83 9f 0e 85 83 9f 0e a1"
#Ans a2 c4

#data = "45 00 00 47 73 88 40 00 40 06 a2 c4 83 9f 0e 85 83 9f 0e a1"

#data = "45 00 05 14 42 a2 21 40 80 01 00 00 c0 a8 00 03 c0 a8 00 01"
#Ans 50b2

import sys
for line in sys.stdin.read().splitlines()[1::]:
    data = line.split()
    ret_checksum = ip_checksum(data,len(data))
    print("%04x" % ret_checksum)