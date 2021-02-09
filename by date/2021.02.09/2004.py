n, m = list(map(int, input().split()))
candidate = {}

def set_candidate():
    target = 5
    cnt = 1

    for _ in range(11):
        candidate[target] = cnt
        target *= 5
        cnt += 1

def init():
    set_candidate()

def get_cnt(num):
    cnt = 0
    temp = num

    items = list(candidate.items())
    items = sorted(items, reverse= True)
    
    for (k, v) in items:
        if(temp % k == 0):
            cnt += v
            break

    return cnt

def get_result():
    up_cnt = 0
    bottom_cnt = 0

    for num in range(n - m + 1, n + 1):
        if(num % 5 == 0):
            up_cnt += get_cnt(num)

    for num in range(1, m + 1):
        if(num % 5 == 0):
            bottom_cnt += get_cnt(num)

    return up_cnt - bottom_cnt

def main():
    # print(candidate)
    print(get_result())
    return

if(__name__=="__main__"):
    init()
    main()