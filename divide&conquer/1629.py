a, b, c = list(map(int, input().split()))

def _1629(a, b, c):
    if(b == 1):
        return a % c

    x1 = _1629(a, b // 2, c)

    if(b % 2 == 0):
        return (x1 **2) % c

    else:
        x2 = (x1 * a) % c
        return (x1 * x2) % c

print(_1629(a, b, c))