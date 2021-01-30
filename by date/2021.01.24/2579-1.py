N = int(input())
stairs = []
result_0 = 0
result_1 = 0

def set_stairs():
    global stairs
    import sys

    for _ in range(N):
        x = int(sys.stdin.readline().rstrip("\n"))
        stairs.append(x)

def print_result():
    print(max(result_0, result_1))

def forward(current, visit, flag):
    global result_0, result_1 

    if(current >= N):
        return

    visit += 1

    if(visit == 3):
        forward(current + 1, visit = 0, flag = flag)
        return

    if(flag == 0):
        result_0 += stairs[current]
        # print("Add : ", current, stairs[current], result_0)
    else:
        result_1 += stairs[current]

    ## 마지막에서 3번째
    if(current == N - 3):
        ## 무조건 2칸
        forward(current + 2, visit = 0, flag = flag)
        return

    ## 마지막에서 2번째
    if(current == N - 2):
        ## 무조건 1칸
        forward(current + 1, visit, flag = flag)
        return

    ## 마지막
    if(current == N - 1):
        return

    ## greedy
    step_1 = current + 1
    step_2 = current + 2
    step_3 = current + 3

    if(current == N - 5):
        if(stairs[step_2] >= stairs[step_1] + stairs[step_3]):
            forward(step_2, visit = 0, flag = flag)
            return

        else:
            forward(step_1, visit, flag)
            return

    ## 1칸
    if(stairs[step_1] + stairs[step_3] >= stairs[step_2] + stairs[step_3]):
        forward(step_1, visit, flag)
        return

    ## 2칸
    if(stairs[step_2] + stairs[step_3] >= stairs[step_1] + stairs[step_3]):
        forward(step_2, visit = 0, flag = flag)
        return

    else:
        print("Error!")

def main():
    forward(0, 0, flag = 0)
    forward(1, 0, flag = 1)
    return
    
if(__name__ == "__main__"):
    set_stairs()
    main()
    print_result()