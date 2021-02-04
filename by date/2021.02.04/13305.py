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
        print(result)
        return result

    current = price[p_ind]
    next_city = 0

    for cp_ind in range(p_ind + 1, N):
        if(current >= price[cp_ind]):
            result += current * sum(length[p_ind:cp_ind])
            next_city = cp_ind
            break
    
    # print(p_ind, current, result, next_city)

    if(next_city != 0):
        recursive(next_city, result)

def main():
    recursive(0, 0)
    return

if(__name__=="__main__"):
    init()
    main()
