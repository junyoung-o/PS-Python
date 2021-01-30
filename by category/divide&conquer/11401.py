import sys
N, K = map(int, sys.stdin.readline().split())
q = 1000000007

def find(k):
    s1, x1 = 1, 0
    s2, x2 = 0, 1
    r1 = q * s1 + k * x1
    r2 = q * s2 + k * x2
    t = r1 // r2

    while (r1%r2 != 0):
        c1, c2, c3 = s1, x1, r1
        s1 = s2
        x1 = x2
        s2 = c1 - s2 * t
        x2 = c2 - x2 * t
        r1 = r2
        r2 = c3 - r2*t
        t = r1 // r2

    if (x2 < 0):
        return x2 + q

    else:
        return x2

def getResult(n, k):
    nResult = 1
    kResult = 1
    for i in range(k):
        nResult *= ((n-i) % q)
        nResult %= q
        kResult *= ((k-i) % q)
        kResult %= q

    kResult = find(kResult)

    return (nResult * kResult) % q

print(getResult(N, K))
