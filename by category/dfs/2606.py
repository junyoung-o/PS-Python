n = int(input())
e = int(input())
result = -1

edge = [[] for _ in range(n+1)]
visit = [0 for _ in range(n+1)]

for i in range(e):
    x, y = list(map(int, input().split()))
    edge[x].append(y)
    edge[y].append(x)

def dfs(v):
    global result
    if(visit[v] == 1):
        return

    result += 1
    visit[v] = 1

    for ne in edge[v]:
        if(visit[ne] == 0):
            dfs(ne)

if(visit[1] == 0):
    dfs(1)

print(result)