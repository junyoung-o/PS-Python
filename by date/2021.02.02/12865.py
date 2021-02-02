N, K = list(map(int, input().split()))
Knap = []
candidate = {}

def set_Knap():
    global Knap
    
    import sys

    for _ in range(N):
        w, v = list(map(int, sys.stdin.readline().split()))
        Knap.append((w, v))

def set_candidate():
    candidate[K] = 0

def init():
    set_Knap()
    set_candidate()
    return

def sort_candidate():
    global candidate
    
    cand = list(candidate.items())

    candidate = dict(sorted(cand, key = lambda x : x[0], reverse = True))

def record_candidate():
    global candidate
    
    for (w, v) in Knap:
        cand = list(candidate.items())
        for remain, values in cand:
            if(remain < w):
                break
            
            if(remain >= w):
                if(remain - w in candidate.keys()):
                    candidate[remain - w] = max(candidate[remain - w], values + v)

                else:
                    candidate[remain - w] = values + v

        sort_candidate()

def print_result():
    values = candidate.values()
    print(max(values))

def main():
    record_candidate()
    print_result()
    return
    
if(__name__ == "__main__"):
    init()
    main()