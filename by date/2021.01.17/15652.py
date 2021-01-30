N, M = list(map(int, input().split()))
edge = [[] for i in range(N+1)]
visited = []

def link():
    for i in range(1, N+1):
        for j in range(i, N+1):
            edge[i].append(j)

def print_result(lists):
    for i in lists:
        print(i, end=" ")
    print()

def dfs(vertex, level):
    global visited
    visited.append(vertex)

    if(level == M):
        print_result(visited)
        visited.pop()
        return

    for node in edge[vertex]:
        dfs(node, level+1)

    visited.pop()

def main():
    link()
    
    for i in range(1, N+1):
        dfs(i, 1)

if(__name__ == "__main__"):
    main()