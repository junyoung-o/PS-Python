N, M = list(map(int, input().split(" ")))
c = True
A = []
B = []
max_r = 0
pre_v = []
for i in range(N):
    A.append(str(input()))

for i in  range(N):
    B.append(str(input()))

print(A, B)

def _1080(A, B):
    print(A)
    global max_r
    for i in range(M-2):
        r = 0
        for j in range(N):
            x = A[j][i:i+3]
            y = B[j][i:i+3]
            for k in range(3):
                if(x[k] != y[k]):
                    r += 1
        if(r >= max_r):
            max_r = r
            pre_v.append([j-2, i])
    print(len(pre_v), pre_v)

_1080(A, B)