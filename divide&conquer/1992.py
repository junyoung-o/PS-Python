n = int(input())
G = []
r = 0

for _ in range(n):
    G.append(list(map(int, input())))

def fff(G, n, x, a, w):
    temp = 0

    if(w == 1):
        for i in range(a,x):
            for j in range(a, x):
                temp += G[i][j]

    if(w == 2):
        for i in range(x,n):
            for j in range(x, n):
                temp += G[i][j]
    if(w == 3):
        for i in range(x, n):
            for j in range(a, x):
                temp += G[i][j]
    if(w == 4):
        for i in range(x, n):
            for j in range(x,n):
                temp += G[i][j]

    if(temp == 0):
        return 0

    if(temp == x*x):
        return 1

    np = x // 2

    lu = fff(G, n, np, a, 1)
    ru = fff(G, n, np, np, 2)
    ld = fff(G, n ,np, a, 3)
    rd = fff(G, n ,np, np, 4)

    x = "({}) ({}) ({}) ({})".format(lu, ru, ld, rd)

    return x

r = fff(G,n, n, 0, 1)

for i in range(n):
    print(G[i])
print(r)