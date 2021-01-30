import sys
sys.setrecursionlimit(100000)

n, m = list(map(int, sys.stdin.readline().split()))
edge = [[] for _ in range(n+1)]
visit = [False for _ in range(n+1)]
result = 0

for _ in range(m):
    x, y = list(map(int, sys.stdin.readline().split()))
    edge[x].append(y)
    edge[y].append(x)

def dfs(v):
    if(visit[v] == True):
        return
        
    visit[v] = True

    for i in edge[v]:
        if(visit[i] == False):
            dfs(i)

for v in range(1,n+1):
    if(visit[v] == False):
        result += 1
        dfs(v)

print(result)