N = int(input())
G = [[] for i in range(N)]
my_G = []
B = [[0 for j in range(N)] for i in range(N)]
v = [0 for i in range(N)]
r = [[0 for j in range(N)] for i in range(N)]

for i in range(N):
    G[i] = list(map(int, input().split()))

for i in range(N):
    for j in range(i+1,N):
        my_G.append([i+1, j+1, G[i][j]])
        
my_G.sort(key = lambda x : x[2])

print(my_G)

for i in range(len(my_G)):
    x = my_G[i]
    a = x[0] - 1
    b = x[1] - 1
    if(x[2] != 0 and v[a] + v[b] < 2):
        v[a] = 1
        v[b] = 1
        r[a][b] = 1
        r[b][a] = 1

min_n = N
min_a = 0
min_b = 0

for i in range(N):
    x = r[i]
    s = sum(x)
    if(min_n > s):
        min_n = s


for i in range(N):
    x = r[i]
    s = sum(x)
    if(min_n == s and min_a == 0):
        min_a = i
    if(min_n == s and min_a != i):
        min_b = i

r[min_a][min_b] = 1
r[min_b][min_a] = 1

print(r)

for i in range(N):
    for j in range(N):
        if(i != j):
            x = r[i][j]
            if(x == 1):
                B[i][j] = 1
            else:
                for k in range(N):
                    y = r[i][k] + r[k][j]
                    if(y >= 2):
                        B[i][j] = 1

print(B)