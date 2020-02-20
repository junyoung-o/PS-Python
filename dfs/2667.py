n = int(input())
arr = []
cnt = 0
c = 0

for i in range(n):
    arr.append(list(map(int,input())))

node = []

for i in range(n):
    for j in range(n):
        if(arr[i][j] == 1):
            x = i * n + j + 1
            node.append(x)

visit = [0 for _ in range(n*n+1)]

def dfs(v):
    global cnt
    if(visit[v] == 1):
        return

    visit[v] = 1
    cnt += 1

    if(v + 1 in node and v % n != 0):
        dfs(v + 1)

    if(v - 1 in node and v % n != 1):
        dfs(v - 1)
        
    if(v + n in node and v <= n**2 - n):
        dfs(v + n)

    if(v - n in node and v > n):
        dfs(v - n)
        

node.sort()
result = []
for i in node:
    if(visit[i] != 1):
        dfs(i)
        c += 1
        result.append(cnt)
    cnt = 0

print(c)
result.sort()
for i in result:
    print(i)