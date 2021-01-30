import sys
sys.setrecursionlimit(100000)
n, m = list(map(int, sys.stdin.readline().split()))

a, b = [], []

for i in range(n):
    x = list(map(int, sys.stdin.readline().split()))
    a.append(x)

m, k = list(map(int, sys.stdin.readline().split()))

for i in range(m):
    x = list(map(int, sys.stdin.readline().split()))
    b.append(x)

def mul_arr(a, b):
    temp = []
    for i in range(n):
        h= []
        for t in range(k):
            s = 0
            for j in range(m):
                x = a[i][j]
                y = b[j][t]
                s += x*y
            h.append(s)
        temp.append(h)

    return temp

def merge_arr(p1, p2):
    temp = []
    for i in range(len(p1)):
        temp.append(p1[i]+p2[i])
    return temp

def divide(a, b):
    x = len(a) // 2
    y = len(b[0]) // 2

    #runtime error, size -> 100
    size = 2
    if(x or y <= size):
        return mul_arr(a, b)

    a1 = a[:x]
    a2 = a[x:]
    b1 = b[:,:y]
    b2 = b[:,y:]

    p1 = divide(a1,b1)
    p2 = divide(a1,b2)
    p3 = divide(a2,b1)
    p4 = divide(a2,b2)

    return  merge_arr(p1, p2) + merge_arr(p3, p4)

result = divide(a,b)

for i in result:
    r = str()
    for j in i:
        r = r + str(j) + " "
        r.rstrip()
    print(r)
