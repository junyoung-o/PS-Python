n = int(input())
edge = []
result = [[0 for _2 in range(n)] for _ in range(n)]

for _ in range(n):
    edge.append(list(map(int, input().split())))

def dfs(s, v):
    if(visit[v] == 1):
        return
    
    visit[v] = 1

    for i in range(len(edge)):
        if(edge[v][i] == 1 and s == i):
            result[s][i] = 1

        if(edge[v][i] == 1 and visit[i] == 0):
            result[s][i] = 1
            dfs(s, i)

for v in range(n):
    visit = [0 for _ in range(n)]
    if(visit[v] == 0):
        dfs(v,v)

for i in result:
    for j in i:
        print(j, end = " ")
    print("")