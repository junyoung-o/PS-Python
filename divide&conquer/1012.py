import sys
sys.setrecursionlimit(1000000)

def dfs(v):
    ind = node.index(v)
    del node[ind]

    if(v % m != 0 and v + 1 in node):
        dfs(v + 1)
    if(v % m != 1 and v - 1 in node):
        dfs(v - 1)
    if(v <= (n-1)*m and v + m in node):
        dfs(v + m)
    if(v > m and v - m in node):
        dfs(v - m)

t = int(input())

for _ in range(t):
    m, n, k = list(map(int, input().split()))
    arr = []
    node = []
    cnt = 0

    for _2 in range(k):
        x, y = list(map(int, input().split()))
        arr.append([y, x])

    for a in arr:
        i, j = a
        n = i * m + j + 1
        node.append(n)
        
    while(len(node) > 0):
        i = node[0]
        dfs(i)
        cnt += 1
    
    print(cnt)
