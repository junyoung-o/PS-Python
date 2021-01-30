N = int(input())
visit = [False for i in range(N*N+1)]
result = 0

def checking(vertex):
    i = (vertex-1) // N
    j = vertex - N * i - 1

    ## 위
    step = 1
    while((i-step) >= 0):
        visit[(i-step)*N + j+1] = True
        step+=1
    ## 아래
    step = 1    
    while((i+step) <= N-1):
        visit[(i+step)*N + j+1] = True
        step+=1

    ## 왼쪽
    step = 1
    while(j-step >=0):
        visit[i*N+(j-step)+1] = True 
        step+=1
    ## 오른쪽
    step = 1
    while(j+step <= N-1):
        visit[i*N+(j+step)+1] = True
        step+=1

    ## -x 왼쪽
    step = 1
    while(i - step >= 0 and j - step >= 0):
        visit[(i-step)*N+(j-step)+1] = True
        step+=1
    ## -x 오른쪽
    step = 1
    while(i + step <= N-1 and j + step <= N-1):
        visit[(i+step)*N+(j+step)+1] = True
        step+=1

    ## x 왼쪽
    step = 1
    while(i + step <= N-1 and j - step >= 0):
        visit[(i+step)*N+(j-step)+1] = True
        step+=1

    ## x 오른쪽
    step = 1
    while(i - step >= 0 and j + step <= N-1):
        visit[(i-step)*N+(j+step)+1] = True
        step+=1


def visiting(vertex, remain_queen):
    global result

    if(visit[vertex]):
        return

    visit[vertex] = True

    if(remain_queen == 0):
        result += 1
        return

    checking(vertex)

    for next_node in range(1, N*N +1):
        if(not visit[next_node]):
            visiting(next_node, remain_queen - 1)

def main():
    global visit

    for start in range(1, N*N + 1):
        visiting(start, N - 1)
        visit = [False for i in range(N*N+1)]
        print("result : ", result)
        print()
    print(result)

if(__name__ == "__main__"):
    main()