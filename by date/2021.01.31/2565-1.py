N = int(input())
linked = []
memo = []
candidate = {}

def set_linked():
    import sys

    for _ in range(N):
        a, b = list(map(int, sys.stdin.readline().split()))
        linked.append((a, b))

def sort_linked():
    global linked

    linked = sorted(linked, key = lambda a : a[1])

def init_memo():
    memo.append(1)

def init_candidate():
    candidate[linked[0][0]]= 0

def get_cnt(num):
    keys = candidate.keys()
    target = 0

    for i in keys:
        if(num > i):
            target = max(target, candidate[i])
    return target

def update(ind, target):
    memo.append(target + 1)
    candidate[linked[ind][0]] = target + 1

def get_lis():
    for ind in range(N):
        a = linked[ind][0]
        target = get_cnt(a)
        update(ind, target)

def get_max():
    return max(memo)

def print_result():
    print(N - get_max())

def main():
    get_lis()
    print_result()
    return
    
if(__name__ == "__main__"):
    set_linked()
    sort_linked()
    main()