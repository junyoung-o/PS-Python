N = int(input())
wine = []
memo = []
memo_max = False

def set_wine():
    import sys
    wine.append(-1)
    for _ in range(N):
        wine.append(int(sys.stdin.readline()))

    return

def set_memo():
    memo.append(-1)
    if(N >= 1):
        memo.append(wine[1])

    if(N >= 2):
        memo.append(wine[1] + wine[2])
        
    if(N >= 3):
        memo.append(max(wine[1] + wine[3], wine[2] + wine[3], memo[2]))
    return

def is_extra():
    if(N == 1):
        print(memo[1])
        return True

    if(N == 2):
        print(memo[2])
        return True

    if(N == 3):
        print(memo[3])
        return True

    return False

def get_max(pre):
    global memo_max

    if(not memo_max):
        for i in range(1, pre - 1):
            memo_max = max(memo_max, memo[i])

    else:
        memo_max = max(memo_max, memo[pre-2])

    return
    
def record():
    for i in range(4, N + 1):
        get_max(i-1)
        memo.append(max(memo[i - 2] + wine[i], ## 2
                        memo_max + wine[i - 1] + wine[i], ## 1
                        ))

    return

def print_result():
    # print(memo)
    print(max(memo))
    return

def main():
    if(not is_extra()):
        record()
        print_result()
        
    return

if(__name__ == "__main__"):
    set_wine()
    set_memo()
    main()