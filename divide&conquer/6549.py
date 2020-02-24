def main():
    n = True
    while(n):
        a, *test = list(map(int, input().split()))
        result = 0

        if(a == 0):
            n = False
            break

        m = len(test) // 2

        

def goqhwk(test):
    while(len(test) > 0):
        x = solve(len(test)-1,len(test), test)
        test.pop()
        if(result < x):
            result = x
    print(result)

def solve(s, e, arr):
    while(s > 0 and cal(arr[s:e]) <= cal(arr[s-1:e])):
        s -= 1
    
    r = cal(arr[s:e])
    
    return r

def cal(arr):
    base = len(arr)
    height = min(arr)
    area = base * height
    return area

main()