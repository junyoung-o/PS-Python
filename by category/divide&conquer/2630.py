n = int(input())
arr = [[] for _ in range(n)]

blue = 0
white = 0

for i in range(n):
    arr[i] = list(map(int, input().split()))

def is_one_zero(arr):
    x = len(arr)
    s = 0

    for i in range(x):
        s+= sum(arr[i])

    if(s == x*x):
        return 1

    if(s == 0):
        return 0

    else:
        return -1

def _2630(arr):
    global blue
    global white

    s = is_one_zero(arr)

    if(s == 1):
        blue +=1
        return
    if(s == 0):
        white += 1
        return

    n = len(arr)
    m = len(arr) // 2

    temp = []
    for i in range(0,m):
        temp.append(arr[i][:m])

    _2630(temp)

    temp = []
    for i in range(0,m):
        temp.append(arr[i][m:])

    _2630(temp)

    temp = []
    for i in range(m,n):
        temp.append(arr[i][:m])

    _2630(temp)

    temp = []
    for i in range(m,n):
        temp.append(arr[i][m:])

    _2630(temp)

    return

_2630(arr)
print(white, blue)