t = int(input())

a, b = -1, -1
result_e = []

def set_e():
    global result_e

    result_e = [0] * (max(a, b) + 1)

    temp_a = a
    temp_b = b

    for i in range(2, max(a, b) + 1):
        temp_aa = 0
        temp_bb = 0

        while(temp_a % i == 0):
            temp_a /= i
            temp_aa += 1

        while(temp_b % i == 0):
            temp_b /= i
            temp_bb += 1
        
        result_e[i] = max(temp_aa, temp_bb)

def init():
    set_e()
    return

def get_result():
    result = 1

    for ind in range(2, len(result_e)):
        if(result_e[ind] != 0):
            result *= ind ** result_e[ind]

    return result

def is_extra():
    if(a == 1 or b == 1):
        print(max(a, b))
        return True
    return False


def print_result(result):
    print(result)

def main():
    global a, b

    for _ in range(t):    
        a, b = list(map(int, input().split()))

        if(not is_extra()):
            init()
            print_result(get_result())

    return

if(__name__=="__main__"):
    main()
