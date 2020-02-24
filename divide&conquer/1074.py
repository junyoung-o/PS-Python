n, x, y = list(map(int, input().split()))

m = pow(2, n)

def fff(a, n, x, y, t, w, z):
    r = -1

    if(a == 1):
        if(x % 2 == 0 and y % 2 == 0):
            return t
        if(x %2 == 0 and y % 2 != 0):
            return t + 1
        if(x % 2 != 0 and y % 2 == 0):
            return t + 2
        else:
            return t + 3

    e = n // 2
    d1 = w + e
    d2 = z + e
    aaa = pow(e, 2)

    if(x < d1 and y < d2):
        r = fff(a - 1, e , x, y, t, w, z)
        return r

    elif(x < d1 and y >= d2):
        r = fff(a - 1, e, x, y, t + aaa, w, z + e)
        return r

    elif(x >= d1 and y < d2):
        r = fff(a - 1, e, x, y, t + 2 * aaa, w + e, z)
        return r

    elif(x >= d1 and y >= d2):
        r = fff(a - 1, e, x, y, t + 3 * aaa, w + e, z + e)
        return r

    return r

re = fff(n, m, x, y, 0, 0, 0)

print(re)