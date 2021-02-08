t = int(input())

def get_mul(m, n):
    result = 1
    for i in range(n):
        result *= (m - i)
    return result

def get_result(n, m):
    source = get_mul(m, n)
    target = get_mul(n, n)

    return source // target

def is_extra(n, m):
    if(n == m):
        print(1)
        return True

    if(n == 1):
        print(m)
        return True
    return False

def main():
    import sys

    for _ in range(t):    
        n, m = list(map(int, sys.stdin.readline().split()))
        if(not is_extra(n, m)):
            print(get_result(n, m))
    return

if(__name__=="__main__"):
    main()
