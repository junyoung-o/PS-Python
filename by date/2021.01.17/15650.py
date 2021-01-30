import queue

N, M = list(map(int, input().split()))
visit = [False for i in range(N+1)]
edge = [[] for i in range(N+1)]
visited = []

def link(node):
    for i in range(node+1, N+1):
        edge[node].append(i)

def set_visit(vertex):
    for i in range(N+1):
        visit[i] = False
    visit[vertex] = True

def print_result(r_list):
    for i in r_list:
        print(i, end =" ")
    print(end ="\n")

def dfs(vertex, cnt):
    global visited

    if(visit[vertex]):
        return

    visit[vertex] = True
    visited.append(vertex)

    if(cnt == M):
        print_result(visited)

        visited = visited[:-1]
        return
    
    for node in edge[vertex]:
        if(not visit[node]):
            dfs(node, cnt+1)
    
        for i in range(node+1, N+1):
            visit[i] = False
    visited = visited[:-1]


def main():
    global visit, visited

    ## M이 1일때
    if(M == 1):
        [print(i) for i in range(1, N+1)]

    ## M이 1이 아닐때
    else:
        ## 1. 자기보다 큰 수 연결
        [link(i) for i in range(1, N+1)]
        
        ## 2. dfs 로 방문
        for vertex in range(1, N+1):
            if(not visit[vertex]):
                dfs(vertex, 1)
                visit = [False for i in range(N+1)]
                visited = []

if(__name__ == "__main__"):
    main()