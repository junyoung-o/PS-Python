N = int(input())
visit = [False for i in range(N*N+1)]
result = 0
half = 0

def checking(vertex):
    check = True
    
    ## 양옆
    ran_min = ((vertex - 1) // N) * N + 1
    ran_max = ((vertex - 1) // N) * N + N

    for i in range(ran_min, ran_max + 1):
        if(visit[i]):
            check = False
            return check

    ## 위, 위쪽 대각
    step = 1
    while(vertex - step * N > 0):
        ## 위
        if(visit[vertex - step * N]): 
            check = False
            return check

        ## 대각
        ran_min = (((vertex - step * N) - 1)//N) * N + 1
        ran_max = (((vertex - step * N) - 1)//N) * N + N

        if(ran_min <= vertex - step * N - step <= ran_max and visit[vertex - step * N - step]):
            check = False
            return check
            
        if(ran_min <= vertex - step * N + step <= ran_max and visit[vertex - step * N + step]):
            check = False
            return check

        step += 1

    ## 아래, 아래대각
    step = 1
    while(vertex + step * N <= N * N):
        ## 아래
        if(visit[vertex + step * N]):
            check = False
            return check

        ## 대각
        ran_min = (((vertex + step * N)-1)//N)*N + 1
        ran_max = (((vertex + step * N)-1)//N)*N + N
        
        if(ran_min <= vertex + step * N - step <= ran_max and visit[vertex + step * N - step]):
            check = False
            return check

        if(ran_min <= vertex + step * N + step <= ran_max and visit[vertex + step * N + step]):
            check = False
            return check

        step += 1
        
    return check

def visiting(vertex, remain_queen, case = "half"):
    global result, half

    if(visit[vertex]):
        return

    if(remain_queen == 0):
        if(case == "half"):
            half += 1
        else:
            result += 1
        return

    visit[vertex] = True

    for next_vertex in range(vertex + 1, N*N + 1):
        if(not visit[next_vertex] and checking(next_vertex)):
            visiting(next_vertex, remain_queen - 1, case)

    visit[vertex] = False
    
    return

def main():
    # 1번
    # for i in range(1, N*N + 1):
    #     visiting(i, N - 1)

    # 2번
    # for num in range(1, N*N + 1, (N + 1)):
    #     # num = (i * N) - (N - i)
    #     ## 대각
    #     visiting(num, N - 1, case = "line")

    #     ## half
    #     ran_min = ((num - 1) // N) * N + ((num - 1) // N) + 1
    #     ran_max = ((num - 1) // N) * N + N
    #     for j in range(ran_min, ran_max):
    #         visiting(j, N-1, case = "half")

    for i in range(1, N):
        num = (i * N) - (N - i)
        ## 대각
        visiting(num, N - 1, case = "line")

        ## half
        ran_min = ((num - 1) // N) * N + i
        ran_max = ((num - 1) // N) * N + N
        for j in range(ran_min, ran_max):
            visiting(j, N-1, case = "half")

    print(result + half)

if(__name__ == "__main__"):
    main()