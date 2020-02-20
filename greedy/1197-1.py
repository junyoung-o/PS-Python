V, E = list(map(int, input().split()))
node = []
visit = [i for i in range(V+1)]
sum_n = 0
link = []
check = 0

for _ in range(E):
    x, y, c = list(map(int, input().split()))
    if(x <= y):
        node.append([x, y, c])
    else:
        node.append([y, x, c])

node.sort(key = lambda x : (x[2],x[0]))
print(node, visit)

def change(a, b):
    if(a > b):
        for i in range(V+1):
            if(visit[i] == a):
                visit[i] = b
    else:
        for i in range(V+1):
            if(visit[i] == b):
                visit[i] = a


def solve(n):
    global sum_n
    global check
    a, b, cost = n
    
    if(visit[a] != visit[b]):
        sum_n += cost
        link.append([a,b])
        check += 1
        change(visit[a], visit[b])


for i in node:
    if(check + 1 >= V):
        break
    else:
        solve(i)

print(link, sum_n, check, visit)