N = int(input())
visit = [False for i in range(N*N+1)]
result = 0

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

def visiting(vertex, remain_queen):
    global result

    if(visit[vertex]):
        return

    if(remain_queen == 0):
        result += 1
        return

    visit[vertex] = True

    for next_vertex in range(vertex + 1, N*N + 1):
        if(not visit[next_vertex] and checking(next_vertex)):
            visiting(next_vertex, remain_queen - 1)

    visit[vertex] = False
    return

def main():
    for i in range(1, N*N + 1):
        visiting(i, N - 1)
    print(result)

if(__name__ == "__main__"):
    main()