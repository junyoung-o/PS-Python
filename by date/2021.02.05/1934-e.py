t = int(input())


def get_G(a, b):
    if(b > a):
        a, b = b, a

    r = a % b
    
    if(r == 0):
        return b

    result = get_G(r, b)

    return result

def get_result(a, b):
    mul = a * b
    div = get_G(a, b)

    return mul // div

def main():
    import sys

    for _ in range(t):
        a, b = list(map(int, sys.stdin.readline().split()))
        print(get_result(a, b))

    return

if(__name__=="__main__"):
    main()