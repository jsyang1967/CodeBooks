# Sample 2
t = [[0, 1, 0], [1, 1, 1], [0, 1, 0]]
u = [[1, 1, 1, 1], [1, 0, 0, 1], [1, 1, 1, 1]]

def kronecker(matrix1, matrix2):
    return [[num1 * num2 for num1 in elem1 for num2 in matrix2[row]] for elem1 in matrix1 for row in range(len(matrix2))]

from sys import stdin
for line in stdin:
    s = list(map(int,line.strip().split()))
    a,b = [],[]
 
    for i in range(s[0]):
        a.append(list(map(int,input().strip().split())))
    for i in range(s[2]):
        b.append(list(map(int,input().strip().split())))

    for row in kronecker(a,b):
        print(" ".join(str(j) for j in row))
        #print(row)
    #print() 