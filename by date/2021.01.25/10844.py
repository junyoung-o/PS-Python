N = int(input())
memo = []
div = 1000000000

def init_memo():
    memo.append(-1)
    memo.append(9)

def is_extra():
    if(N == 1):
        print(memo[1])
        return True

    return False

def record_memo():
    for num in range(2, N + 1):
        memo.append(memo[num - 1] * 2 - (num - 1))

def print_result():
    print(memo[N] % div)

def main():
    init_memo()

    if(not is_extra()):
        record_memo()
        print_result()
        
    return

if(__name__ == "__main__"):
    main()
    