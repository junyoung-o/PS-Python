N, K = list(map(int, input().split()))
coin = []



def set_coin():
    global coin

    import sys

    for _ in range(N):
        coin.append(int(sys.stdin.readline()))

    coin = filter(lambda x : x <= K, coin)
    coin = sorted(coin, reverse= True)

def init():
    set_coin()

def get_result():
    target = K
    result = 0

    for cand in coin:
        result += target // cand
        target -= cand * (target // cand)

    return result

def main():
    print(get_result())
    return

if(__name__=="__main__"):
    init()
    main()
