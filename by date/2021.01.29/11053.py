N = int(input())
A = []
memo = []
candidate = {}

def set_A():
    global A
    
    import sys
    A.append(-1)
    A += list(map(int, sys.stdin.readline().split()))

def set_memo():
    memo.append(-1)
    memo.append(1)

def set_candidate():
    candidate[-1] = 0
    candidate[A[1]] = 1

def update_memo_candidate(ind, target):
    memo.append(target)
    candidate[A[ind]] = target

def get_cand(num):
    keys = candidate.keys()
    keys = sorted(keys, reverse=True)
    
    result = 0
    for i in keys:
        if(num > i):
            result = max(candidate[i], result)

    return result

def record():
    for ind in range(2, N+1):
        target = get_cand(A[ind])

        if(A[ind - 1] < A[ind]):
            target = max(memo[ind - 1], target)

        target += 1

        update_memo_candidate(ind, target)

def is_extra():
    if(N == 1):
        print(memo[1])
        return True
    return False

def print_result():
    # print(candidate)
    print(max(memo))

def main():
    if(not is_extra()):
        record()
        print_result()

if(__name__ == "__main__"):
    set_A()
    set_memo()
    set_candidate()
    main()