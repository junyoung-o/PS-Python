import sys
import queue

def set_node():
    for i in range(n):
        for j in range(m):
            x = i * m + (j + 1)
            node[x] = arr[i][j]

def link_n():
    for e in range(1, n*m +1):
        up = e - m
        down = e + m
        left = e - 1
        right = e + 1

        if(e <= m):
            if(e == 1):
                edge[e] = [down, right]
            elif(e == m):
                edge[e] = [down, left]
            else:
                edge[e] = [down, left, right]

        elif(e >= (n-1) * m + 1):
            if(e == (n-1) * m + 1):
                edge[e] = [up, right]
            elif(e == n * m):
                edge[e] = [up, left]
            else:
                edge[e] = [up, left, right]
        elif(e % m == 1):
            edge[e] = [up, down, right]

        elif( e % m == 0):
            edge[e] = [up, down, left]

        else:
            edge[e] = [up, down, left, right]

    return

def set_visit():
    visit = [False for _ in range(n * m + 1)]
    return visit

def bfs(arr):
    global cnt

    q = queue.Queue()
    q.put(arr)

    while(q.empty() != True):
        x = q.get()

        if(len(x) == 0):
            break

        next = []
        for i in x:
            for v in edge[i]:
                if(visit[v] == False):
                    visit[v] = True
                    if(node[v] == 0):
                        next.append(v)
        q.put(next)
        cnt += 1

    return


m, n = list(map(int, sys.stdin.readline().split()))
arr = []
edge = [0 for _ in range(0, m*n+1)]
node = {}
cz = 0
one_n = []

for _ in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))

link_n()
set_node()

for k, v in node.items():
    if(v == 0):
        cz += 1
    if(v == 1):
        one_n.append(k)

if(cz == 0):
    print(0)

else:
    visit = set_visit()
    cnt = -1
    can = False
    bfs(one_n)

    for i in range(1,n*m+1):
        if(visit[i] == False and node[i] == 0):
            print(-1)
            can = True
            break

    if(can == False):
        print(cnt)