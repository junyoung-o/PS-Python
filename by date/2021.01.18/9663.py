N = int(input())
visit = [False for i in range(N*N +1)]
result = 0

def count_remain():
    global result

    cnt = 0
    for i in visit:
        if(i == False):
            cnt += 1

    result += (cnt)

def visiting(node, remain_queen):
    global result

    if(visit[node]):
        return

    visit[node] = True


    if(remain_queen == 0):
        count_remain()
        return

    i = (node - 1)//N
    j = node - i*N - 1

    ## 가로
    for row in range(i*N+1, i*N+N +1):
        visit[row] = True

    ## 세로
    for col in range(N):
        visit[col*N+j+1] = True

    ## -x 대각
    t = 1
    while(((i - t)*N + (j - t) + 1 > 0) and (i - t >= 0 and j - t >= 0)):
        visit[(i - t)*N + (j - t) + 1] = True
        t += 1
    t = 1
    while(((i + t)*N + (j + t) + 1 <= N*N) and (i + t <= N-1 and j + t <= N-1)):
        visit[(i + t)*N + (j + t) + 1] = True
        t += 1

    ## x 대각
    t = 1
    while(((i - t)*N + (j + t) + 1 >= N) and (i - t >= 0 and j + t <= N-1)):
        visit[(i - t)*N + (j + t) + 1] = True
        t += 1
    t = 1
    while(((i + t)*N + (j - t) + 1 <= (N*N - N + 1)) and (i + t <= N-1 and j - t >= 0)):
        visit[(i + t)*N + (j - t) + 1] = True
        t += 1

    for next_node in range(1, N*N+1):
        if(not visit[next_node]):
            visiting(next_node, remain_queen - 1)

def main():
    global visit

    if(N == 1):
        print(1)
    else:
        for start in range(1, N*N +1):
            visiting(start, N - 1)
            visit = [False for i in range(N*N +1)]

        print(result)

if(__name__ == "__main__"):
    main()