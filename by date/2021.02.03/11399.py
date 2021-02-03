N = int(input())
time = []

def sort_time():
    global time
    time = sorted(time)

def set_time():
    global time
    time = list(map(int, input().split()))
    sort_time()

def init():
    set_time()
    return
    
def get_result():
    result = 0
    iter_x = N

    for t in time:
        result += iter_x * t
        iter_x -= 1

    return result

def main():
    print(get_result())
    return

if(__name__=="__main__"):
    init()
    main()
