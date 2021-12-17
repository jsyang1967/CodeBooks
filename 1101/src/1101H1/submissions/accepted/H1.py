import sys
n = int(sys.stdin.readline())

def solve():
    data = sys.stdin.readline().replace("\n","").split("/")
    ip = [int(_) for _ in data[0].split(".")]
    mask = [int(_) for _ in data[1].split(".")]
    re1 = []
    re2 = []
    for i in range(len(ip)):
        re1.append(andop(ip[i],mask[i]))
        re2.append(ornot(ip[i],mask[i]))
    IP1 = ".".join(str(_) for _ in re1)
    IP2 = (".".join(str(_) for _ in re2))
    print(IP1 + "/" + IP2)
#    print(".".join(str(_) for _ in re1))
#    print(".".join(str(_) for _ in re2))

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