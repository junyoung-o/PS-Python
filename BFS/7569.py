# import
import sys
import queue


# function
def set_node():
    for k in range(h):
        for i in range(n):
            for j in range(m):
                x = i * m + (j + 1) + k * (n * m)
                node[x] = arr[k][i][j]
    return


def set_edge(v):
    maximun = (h * m * n) + 1
    up = v - m
    down = v + m
    left = v - 1
    right = v + 1
    ulayer = v + n * m
    dlayer = v - n * m

    if (up <= 0):
        up = 0
    if (left <= 0):
        left = 0
    if (dlayer <= 0):
        dlayer = 0
    if (down >= maximun):
        down = 0
    if (right >= maximun):
        right = 0
    if (ulayer >= maximun):
        ulayer = 0

    if (v % m == 1):
        if ((v % (m * n)) <= m):
            edge[v] = [down, right, ulayer, dlayer]
        elif ((v % (m * n)) > m * (n - 1)):
            if (v == 30):
                print("check")
            edge[v] = [up, right, ulayer, dlayer]
        else:
            edge[v] = [up, down, right, ulayer, dlayer]

    elif (v % m == 0):
        if ((v % (m * n)) <= m and (v % (m * n)) != 0):
            edge[v] = [down, left, ulayer, dlayer]
        elif ((v % (m * n)) > m * (n - 1) or (v % (m * n)) == 0):
            edge[v] = [up, left, ulayer, dlayer]
        else:
            edge[v] = [up, down, left, ulayer, dlayer]

    elif ((v % (m * n)) > m * (n - 1)):
        edge[v] = [up, left, right, ulayer, dlayer]

    elif ((v % (m * n)) <= m):
        edge[v] = [down, left, right, ulayer, dlayer]

    else:
        edge[v] = [up, down, left, right, ulayer, dlayer]


def bfs(vertex_list):
    global cnt

    q = queue.Queue()
    q.put(vertex_list)

    while (q.empty() != True):
        x = q.get()

        if (len(x) == 0):
            break

        next = []
        for i in x:
            for v in edge[i]:
                if (visit[v] == False and v != 0):
                    visit[v] = True
                    if (node[v] == 0):
                        next.append(v)
        q.put(next)
        cnt += 1

    return


# main
m, n, h = list(map(int, sys.stdin.readline().split()))
arr = []
start_n = []
cz = 0

for k in range(h):
    temp = []
    for _ in range(n):
        temp.append(list(map(int, sys.stdin.readline().split())))
    arr.append(temp)

node = {"0": 0}
set_node()

for k, v in node.items():
    if (v == 1):
        start_n.append(k)
    if (v == 0):
        cz += 1

if (cz == 0):
    print(0)

else:
    cnt = -1

    visit = [False for _ in range(n * m * h + 1)]

    edge = [[] for i in range(n * m * h + 1)]

    for v in range(1, m * n * h + 1):
        set_edge(v)

    check = True

    bfs(start_n)

    for i in range(1, m * n * h + 1):
        if (visit[i] == False and node[i] == 0):
            print(-1)
            check = False
            break
    if (check):
        print(cnt)