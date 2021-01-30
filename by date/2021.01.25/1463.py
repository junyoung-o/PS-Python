N = int(input())
memo = []

def init_memo():
    memo.append(-1)
    memo.append(0)
    memo.append(1)
    memo.append(1)

def record():
    for i in range(4, N + 1):
        value = 10000000001

        if(i % 3 == 0):
            value = min(memo[i - 1], memo[i // 3])

        if(i % 2 == 0):
            value = min(value, memo[i // 2])

        value = min(memo[i - 1], value)

        value += 1
        memo.append(value)

def extra():
    if(N == 1):
        print(memo[1])
        return False

    if(N == 2):
        print(memo[2])
        return False

    if(N == 3):
        print(memo[3])
        return False

    return True

def print_result():
    print(memo.pop())

def main():
    init_memo()

    if(extra()):
        record()
        print_result()
        
    return
    
    
    
if(__name__ == "__main__"):
    main()
    