def cal(arr):
    if(len(arr) == 0):
        return 0

    base = len(arr)
    height = min(arr)

    area = base * height
    return area

def middle(arr, m):
    r = m + 1
    l = m
    
    while(cal(arr[l:r]) <= cal(arr[l:r + 1]) and r < len(arr)):
        r += 1
    
    while(cal(arr[l:r]) <= cal(arr[l-1:r]) and l > 0):
        l -= 1

    area = cal(arr[l:r])
    return area

def dac(arr):
    area = 0

    if(len(arr) == 0):
        return area

    if(len(arr) == 1):
        area = arr[0]
        return area

    m = len(arr) // 2

    area = middle(arr, m)

    left = dac(arr[:m])
    right = dac(arr[m:])
    area = max(left, right, area)
    return area
    

def start():
    n = True

    while(n):
        a, *test = list(map(int, input().split()))
        if(a == 0):
            n = False
            break
        else:
            area = dac(test)
            print(area)

start()