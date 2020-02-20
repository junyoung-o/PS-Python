N = int(input())
K = []

for i in range(N):
    x = int(input())
    K.append(x)

K.sort()

max_W = 0

for i in range(N):
    n = K[i] * (N-i)
    if(max_W < n):
        max_W = n

print(max_W)