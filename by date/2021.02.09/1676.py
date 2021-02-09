n = int(input())

def init():
    return

def get_factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i

    return result

def get_result(f):
    str_f = str(f)
    result = 0

    ind = 1
    while(str_f[-ind] == "0"):
        result += 1
        ind += 1

    return result

def main():
    f = get_factorial(n)
    print(get_result(f))
    return

if(__name__=="__main__"):
    init()
    main()