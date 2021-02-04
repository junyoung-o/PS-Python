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

def visiting_city():
    next_city = 0
    result = 0

    for current_city in range(N):
        if(next_city == N - 1):
            break

        if(next_city <= current_city):
            for compare_city in range(current_city + 1, N):
                if(compare_city == N - 1):
                    next_city = N - 1
                
                if(price[current_city] <= price[compare_city]):
                    result += price[current_city] * length[compare_city - 1]

                if(price[current_city] > price[compare_city]):
                    result += price[current_city] * length[compare_city - 1]
                    next_city = compare_city
                    break

    print(result)

def is_extra():
    if(N == 2):
        print(price[0] * length[0])
        return True
    return False

def main():
    if(not is_extra()):
        visiting_city()
    return

if(__name__=="__main__"):
    init()
    main()
