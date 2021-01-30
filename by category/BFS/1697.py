import queue
n, k = list(map(int, input().split()))

def bfs(v):
    global r
    check = True
    if(v == k):
        return

    visit[v] = True
    q = queue.Queue()
    h = list()

    if(v + 1 <= maxn):
        h.append(v + 1)
    if(v - 1 >= 0):
        h.append(v - 1)
    if(v * 2 <= maxn):
        h.append(v * 2)

    q.put(h)

    while(q.empty() != True):
        next_list = q.get()
        h = []
        r += 1
        for next in next_list:
            if(next == k):
                check = False
                q.queue.clear()

            elif(visit[next] == False):
                visit[next] = True
                if(next + 1 <= maxn):
                    if(visit[next + 1] == False):
                        h.append(next + 1)
                if(next * 2 <= maxn):
                    if(visit[next * 2] == False):
                        h.append(next * 2)
                if(next - 1 >= 0):
                    if(visit[next - 1] == False):
                        h.append(next - 1)
        if(check):
            q.put(h)
        else:
            q.queue.clear()

maxn = 100000
r = 0
visit = [False for _ in range(maxn + 1)]
bfs(n)
print(r)