N, M = list(map(int, input().split()))
edge = [[] for i in range(N+1)]
visited = []

def link():
    for i in range(1, N+1):
        for j in range(1, N+1):
            edge[i].append(j)

def print_result(result_list):
    for i in result_list:
        print(i, end=" ")
    print(end="\n")

def dfs(vertex, cnt):
    global visited

    visited.append(vertex)

    if(cnt == M):
        print_result(visited)
        visited = visited[:-1]
        return
    
    for node in edge[vertex]:
        dfs(node, cnt + 1)

    visited = visited[:-1]

def main():
    link()
    
    for i in range(1, N+1):
        dfs(i, 1)

if(__name__ == "__main__"):
    main()