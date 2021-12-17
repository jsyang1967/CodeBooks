import sys
n = int(sys.stdin.readline())

def len2mask(len):
    """Convert a bit length to a dotted netmask (aka. CIDR to netmask)"""
    mask = ''
    if not isinstance(len, int) or len < 0 or len > 32:
        print("Illegal subnet length: %s (which is a %s)" % (str(len), type(len).__name__))
        return None
    
    for t in range(4):
        if len > 7:
            mask += '255.'
        else:
            dec = 255 - (2**(8 - len) - 1)
            mask += str(dec) + '.'
        len -= 8
        if len < 0:
            len = 0
    
    return mask[:-1]

def solve():
    data = sys.stdin.readline().replace("\n","").split("/")
    #print(data[0],data[1])
    ip = [int(_) for _ in data[0].split(".")]
    #print("ip",ip)
    data1=len2mask(int(data[1]))
    #print("data1",data1)
    mask = [int(_) for _ in data1.split(".")]
    re1 = []
    re2 = []
    for i in range(len(ip)):
        re1.append(andop(ip[i],mask[i]))
        re2.append(ornot(ip[i],mask[i]))
    IP1 = ".".join(str(_) for _ in re1)
    IP2 = (".".join(str(_) for _ in re2))
    print(IP1 + "/" + IP2)

def ornot(n1,n2):
   st1 = bin(n1).replace("0b","").zfill(8)
   st2 = bin(n2).replace("0b","").zfill(8)
   re = ""
   for i in range(len(st1)):
      if st1[i] == "0" and st2[i] == "1": re += "0"
      else: re += "1"
   return int(re,2)

def andop(str1,str2):
    st1 = bin(str1).replace("0b","").zfill(8)
    st2 = bin(str2).replace("0b","").zfill(8)
    re = []
    for i in range(len(st1)):
        if st1[i] == "1" and st2[i] == "1": re.append("1")
        else: re.append("0")
    return int("".join(_ for _ in re),2)



for i in range(n):
    solve()