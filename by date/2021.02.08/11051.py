N, K = list(map(int, input().split()))

def init():
    return

def get_mul(a, b):
    result = 1
    for i in range(b):
        result *= (a - i)
    return result

def get_result():
    source = get_mul(N, K)
    target = get_mul(K, K)

    return (source // target) % 10007

def main():
    # print_result()
    print(get_result())
    return

if(__name__=="__main__"):
    init()
    main()
