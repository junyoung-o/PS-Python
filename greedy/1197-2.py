from queue import PriorityQueue

qu = PriorityQueue()

V, E = list(map(int, input().split()))
visit = [0 for _ in range(V+1)]
node = [[] for _ in range(V+1)]
check = 0
sum_n = 0

for _ in range(E):
    a, b, c = list(map(int, input().split()))
    node[a].append([c, b])
    node[b].append([c, a])

def solve(a):
    global sum_n
    if(visit[a] != 0):
        return

    visit[a] = 1

    for i in node[a]:
        qu.put(i)

    while(qu.empty() == False):
        cost, n_node = qu.get()
        if(visit[n_node] == 0):
            visit[n_node] = 1
            sum_n += cost
            for i in node[n_node]:
                qu.put(i)


for i in range(1,V+1):
    if(visit[i] == 0):
        solve(i)

print(sum_n)