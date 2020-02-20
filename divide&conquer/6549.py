def checkav(arr):
    temp = arr[0]
    ck = 1

    for i in arr:
        if(i != temp):
            ck = 0
            break

    return ck

def dicon(arr):
    if(len(arr) == 0):
        return 0

    if(len(arr) == 1):
        return arr[0]

    if(len(arr) == 2):
        temp = min(arr) * 2
        return temp

    ch = checkav(arr)

    if(ch == 1):
        rf = arr[0] * len(arr)
        return rf

    x = arr.index(min(arr))

    left = dicon(arr[:x])
    right = dicon(arr[x + 1:])

    r = max(left, right)

    return r

t = True

while(t):
    test = list(map(int, input().split()))

    if(sum(test) == 0):
        t = False
        break
    
    ch = checkav(test)

    if(ch == 1):
        re = test[0] * len(test)
    else:
        re = dicon(test)

    print(re)
