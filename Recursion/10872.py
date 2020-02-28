n = int(input())

def _10870(n, s, e):
    if(n == 0):
        return 1

    if(n == 1):
        return s

    if(n == 2):
        return s * e

    m = n // 2

    x1 = _10870(m, s, m + s - 1)

    if((e-s) % 2 == 0):
        x2 = _10870(m + 1, m + s, e)

    else:
        x2 = _10870(m, m + s, e)

    return x1*x2

result = _10870(n, 1, n)

print(result)
