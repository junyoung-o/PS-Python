#만약 높이가 모두 같다면
def check(arr):
    s = sum(arr)
    area = len(arr) * min(arr)

    if(s == area):
        return area
    else:
        return 0

def _6549(arr):
    area = 0

    #degenerate case
    if(len(arr) == 0):
        return area

    #smart degenerate case
    smart = check(arr)

    if(smart != 0):
        area = smart
    
    else:
        height = min(arr)
        base = len(arr)
        area = base * height
    
    #divide
    min_x = arr.index(min(arr))

    #높이가 작은 걸 기준으로 짤라서 왼쪽, 오른쪽 넓이 최댓값 return
    left = _6549(arr[:min_x])
    right = _6549(arr[min_x + 1:])
    
    #conquer
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
            if(check(test) != 0):
                result = check(test)
            else:
                result = _6549(test)

            print(result)

start()