import math

N = int(input())
numbers = []
result = []

def set_numbers():
    global numbers

    import sys
    for _ in range(N):
        numbers.append(int(sys.stdin.readline()))

def init():
    set_numbers()
    return

def get_G(a, b):
    if(b > a):
        a, b = b, a
    if(b == 0):
        return a

    r = a % b
    if(r == 0):
        return b

    result = get_G(r, b)

    return result

def get_common_G(copy_list):
    gcd = copy_list[0]
    for i in range(1, len(copy_list)):
        gcd = get_G(copy_list[i], gcd)
    return gcd

def minus_min():
    global result

    copy_list = numbers.copy()
    min_num = min(copy_list)

    for i in range(N):
        copy_list[i] -= min_num

    target = get_common_G(copy_list)
    
    result.append(target)
    for ele in range(2, target // 2 + 1):
        if(target % ele  == 0 and ele not in result):
            result.append(ele)

    return result

def print_result():
    global result
    result = sorted(result)
    [print(i, end = " ") for i in result]

def main():
    minus_min()
    print_result()
    return

if(__name__=="__main__"):
    init()
    main()
