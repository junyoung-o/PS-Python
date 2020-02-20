n, m, v = list(map(int, input().split()))
edge = [[] for _ in range(n+1)]

for i in range(m):
    x, y = list(map(int, input().split()))
    edge[x].append(y)
    edge[y].append(x)

def DFS(v):
    if(visit[v] == 1):
        return
    
    result_d.append(v)
    visit[v] = 1

    for i in edge[v]:
        if(visit[i] != 1 and len(edge[i]) > 0):
            DFS(i)

def start_d():
    DFS(v)

def BFS(v):
    if(visit[v] == 1):
        return

    visit[v] = 1
    
    result_b.append(v)
    q.put(edge[v])

    while(q.empty() != True):
        lists = q.get()
        for i in lists:
            if(visit[i] != 1):
                result_b.append(i)
                visit[i] = 1
                q.put(edge[i])

def start_b():
    BFS(v)

for i in range(len(edge)):
    edge[i].sort()

visit = [0 for _ in range(n+1)]
result_d = []
start_d()

import queue
q = queue.Queue()
result_b = []
visit = [0 for _ in range(n+1)]
start_b()


# print("--------------------------")
result = str()
for i in result_d:
    result = result + str(i) + " "
print(result.rstrip(" "))

result = str()
for i in result_b:
    result = result + str(i) + " "
print(result.rstrip(" "))

# print("-----------------")
# print(edge)