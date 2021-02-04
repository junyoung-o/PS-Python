N = int(input())
price = []
length = []

def set_price():
    global price
    price = list(map(int, input().split()))

def set_length():
    global length
    length = list(map(int, input().split()))

def init():
    set_length()
    set_price()
    return

def recursive(p_ind, result):
    if(p_ind >= N - 1):
        # print(result)
        return result

    if(p_ind == 0 and result != 0):
        # print("deep : ", result)
        return result

    current = price[p_ind]
    next_city = 0

    for cp_ind in range(p_ind + 1, N):
        if(current <= price[cp_ind]):
            result += length[cp_ind - 1] * current
        
        if(current > price[cp_ind]):
            result += length[cp_ind - 1] * current
            next_city = cp_ind
            break
        
    # print("visit : ", p_ind, current, result, next_city)
    
    result = recursive(next_city, result)

    return result

def is_extra():
    if(N == 2):
        print(price[0] * length[0])
        return True
    return False

def main():
    if(not is_extra()):
        print(recursive(0, 0))
    return

if(__name__=="__main__"):
    init()
    main()
