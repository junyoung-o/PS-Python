V, E = list(map(int, input().split()))
node = []
U = [i+1 for i in range(V)]
sum_n = 0
check = 0

for _ in range(E):
    x, y, c = list(map(int, input().split()))
    node.append([x, y, c])

# print(node)

node.sort(key = lambda x : x[2])

def solve(a):
    global sum_n
    global check
    n1 = a[0]
    n2 = a[1]
    cost = a[2]
    if(U[n1-1] != U[n2-1]):
        print("link : {} - {}".format(n1,n2))
        sum_n += cost
        check += 1
        if(U[n1-1] >= U[n2-1]):
            U[n2-1] = U[n1-1]
        else:
            U[n1-1] = U[n2-1]
        print("U : {}".format(U))

for i in node:
    if(check > V or check + 1 == V):
        break
    if(check < V):
        solve(i)

print(sum_n, U)