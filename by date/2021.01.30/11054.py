N = int(input())
A = []
A_reverse = []
reverse_memo = []
memo = []
candidate = {}
result = []

def set_A():
    global A, A_reverse
    A = [-1] + list(map(int, input().split()))
    A_reverse = [-1] + list(reversed(A[1:]))

def set_memo():
    memo.append(0)
    reverse_memo.append(0)

def set_candidate():
    global candidate

    candidate = {}
    candidate[-1] = 0

def get_premax(num):
    candidate_keys = candidate.keys()

    target = 0
    for t in candidate_keys:
        if(num > t):
            target = max(target, candidate[t])

    return target

def update_candidate(num, target):
    candidate[num] = target + 1

def update_reverse_memo(target):
    reverse_memo.append(target + 1)

def update_memo(target):
    memo.append(target + 1)

def set_result():
    global result

    for ind in range(1, N+1):
        result.append(memo[ind] + reverse_memo[N - ind + 1] - 1)

def record():
    for ind in range(1, N+1):
        target = get_premax(A_reverse[ind])
        update_reverse_memo(target)
        update_candidate(A_reverse[ind], target)
        
    set_candidate()

    for ind in range(1, N+1):
        target = get_premax(A[ind])
        update_candidate(A[ind], target)
        update_memo(target)

def print_result():
    print(max(result))

def main():
    record()
    set_result()
    print_result()
    return
    
if(__name__ == "__main__"):
    set_A()
    set_memo()
    set_candidate()
    main()