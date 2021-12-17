def hamming(s1,s2):
    result=0
    if len(s1)!=len(s2):
        print("String are not equal")
    else:
        for x,(i,j) in enumerate(zip(s1,s2)):
            if i!=j:
                #print(f'char not math{i,j}in {x}')
                result+=1
    return result

t = int(input())
for _ in range(t):
    s1=input()
    s2=input()
    print(hamming(s1,s2))
