n = int(input())
arr = []

for _ in range(n):
    x, y = list(map(int, input().split()))
    arr.append([x, y])

def cal(a, b):
    x1, y1 = a
    x2, y2 = b

    n1 = pow(x1 - x2, 2)
    n2 = pow(y1 - y2, 2)

    result = n1 + n2

    return result


def _2261(arr):
    min_r = 500
    
    n = len(arr)
    
    if(n == 1):
        return min_r

    if(n == 2):
        min_r = cal(arr[0], arr[1])
        return min_r
    
    m = n // 2
    
    left = _2261(arr[:m])
    right = _2261(arr[m:])
    middle = cal(arr[m-1],arr[m])

    result = min(left, right, min_r, middle)

    return result

arr.sort(key = lambda x : (x[0],x[1]))
hmm = _2261(arr)
arr.sort(key = lambda x : (x[1],x[0]))
hmm2 = _2261(arr)

result = min(hmm, hmm2)

print(result)