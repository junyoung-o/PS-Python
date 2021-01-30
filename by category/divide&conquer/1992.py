n = int(input())
G = []
r = 0

def cal(G):
    temp = 0

    for i in G:
        temp += i.count(1)
    return temp

for _ in range(n):
    G.append(list(map(int, input())))

def solve(G,n, a):
    temp = cal(G)
    # print("G : {}, n : {}, a : {}".format(G, n, a))
    if(temp == 0):
        return 0

    if(temp == n*n):
        return 1

    if(n == 2):
        lu = G[0][0]
        ru = G[0][1]
        ld = G[1][0]
        rd = G[1][1]
    
    else:
        x = n // 2

        Gp = []
        for i in range(a,x):
            Gp.append(G[i][:x])
        
        lu = solve(Gp,x,a)
        Gp = []

        for i in range(a,x):
            Gp.append(G[i][x:])
        ru = solve(Gp,x,a)
        Gp = []

        for i in range(x,n):
            Gp.append(G[i][:x])
        
        ld = solve(Gp,x,a)
        Gp = []

        for i in range(x,n):
            Gp.append(G[i][x:])
        rd = solve(Gp,x,a)

    re = "({}{}{}{})".format(lu,ru,ld,rd)

    return re

r = solve(G,n,0)
print(r)