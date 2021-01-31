N = int(input())
A = []
memo = [0 for i in range(1001)]

def set_A():
    global A
    
    A = list(map(int, input().split()))

def record():
    for ind in range(N):
        for pre in range(ind):
            if(A[pre] < A[ind] and memo[pre] > memo[ind]):
                memo[ind] = memo[pre]
        memo[ind] += 1

def print_result():
    print(max(memo))

def main():
    record()
    print_result()
    return
    
if(__name__ == "__main__"):
    set_A()
    main()