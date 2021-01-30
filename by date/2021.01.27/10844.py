N = int(input())
candidate = {}
memo = []
div = 1000000000

def init_memo():
    memo.append(-1)
    memo.append(9)
    memo.append(17)

def init_candidate():
    global candidate
    candidate = {9 : 1, 0 : 1}

def get_minus():
    global candidate

    minus = 0

    new_candidate = {}

    candidate_list = candidate.keys()

    for leaf in candidate_list:
        up = leaf + 1
        down = leaf - 1

        if(up < 10):
            try:
                new_candidate[up] += candidate[leaf]
            except:
                new_candidate[up] = candidate[leaf]

            minus += candidate[leaf]

        if(down == 0):
            try:
                new_candidate[down] += candidate[leaf]

            except:
                new_candidate[down] = candidate[leaf]
            
        elif(down > 0):
            try:
                new_candidate[down] += candidate[leaf]

            except:
                new_candidate[down] = candidate[leaf]
            
            minus += candidate[leaf]

    candidate = new_candidate

    return minus

def is_extra():
    if(N == 1):
        print(memo[1])
        return True

    if(N == 2):
        print(memo[2])
        return True

    return False

def record():
    for i in range(3, N+1):
        memo.append(memo[i-1]*2 - get_minus())

def print_result():
    print(memo[N] % div)

def main():
    if(not is_extra()):
        record()
        print_result()
        
if(__name__ == "__main__"):
    init_memo()
    init_candidate()
    main()
    