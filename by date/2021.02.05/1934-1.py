t = int(input())

def get_result(a, b):
    result = a * b
    a_copy = a
    b_copy = b

    for i in range(2, min(a, b) + 1):
        div = min(a, b) + 2 - i
        if(a_copy % div == 0 and b_copy % div == 0 and result % div == 0):
            a_copy /= div
            b_copy /= div
            result /= div

    return int(result)

def is_extra(a, b):
    if(a == 1 or b == 1):
        print(max(a, b))
        return True

    if(a == b):
        print(a)
        return True

    return False

def main():
    import sys

    for _ in range(t):
        a, b = list(map(int, sys.stdin.readline().split()))
        if(not is_extra(a, b)):
            print(get_result(a, b))

    return

if(__name__=="__main__"):
    main()