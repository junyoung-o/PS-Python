import sys

n, b = list(map(int, sys.stdin.readline().split()))

a = []

for _ in range(n):
    a.append(list(map(int, sys.stdin.readline().split())))

# matmul(a, b)
def mul_arr(a, b):
    n = len(a)
    m = len(a[0])
    k = len(b[0])
    temp = []

    for i in range(n):
        h = []
        for t in range(k):
            s = 0
            for j in range(m):
                x = a[i][j]
                y = b[j][t]
                s += x * y
            h.append(s % 1000)
        temp.append(h)
    return temp

# a^b
def _10830(b):
    global a

    if(b == 1):
        return a

    if(b == 2):
        x = mul_arr(a, a)
        return x

    m = b // 2

    x1 = _10830(m)

    if(b % 2 == 0):
        x2 = x1

    else:
        x2 = mul_arr(x1, a)

    result = mul_arr(x1, x2)

    return result

result = _10830(b)

for i in result:
    s = str()
    for j in i:
        s += str(j% 1000) + " "
        s.rstrip()
    print(s)