N = int(input())
stairs = []
result_1 = 0
result_2 = 0

def set_stairs():
    global stairs
    import sys

    for _ in range(N):
        x = int(sys.stdin.readline().rstrip("\n"))
        stairs.append(x)

def print_result():
    print(max(result_1, result_2))

def forward(current, flag, visit, candidate):
    global result_1, result_2

    if(current >= N):
        return

    # print("Visit : ", stairs[current], visit, candidate)

    ## N - 3 일 때
    if(current == N - 3):
        forward(current + 2, flag = flag, visit = 2, candidate = candidate + stairs[current + 2])
        return

    ## N - 2 일 때
    if(current == N - 2):
        forward(current + 1, flag = flag, visit = 1, candidate = candidate + stairs[current + 1])
        return

    ## N - 1 일 때
    if(current == N - 1):
        if(flag == 1):
            result_1 = max(candidate,result_1)
            return

        if(flag == 2):
            result_2 = max(candidate, result_2)
            return

    if(visit == 1):
        forward(current + 2, flag = flag, visit = 2, candidate = candidate + stairs[current + 2])
        return
        
    if(visit == 2):
        forward(current + 1, flag = flag, visit = 1, candidate = candidate + stairs[current + 1])
        forward(current + 2, flag = flag, visit = 2, candidate = candidate + stairs[current + 2])
        return
        
    return

def main():
    forward(0, flag = 1, visit = 2, candidate = stairs[0])
    forward(1, flag = 2, visit = 2, candidate = stairs[1])
    return
    
if(__name__ == "__main__"):
    set_stairs()
    main()
    print_result()
    