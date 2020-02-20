N, M = list(map(int, input().split(" ")))
c = True
A = []
B = []
max_r = -1
pre_v = []
for i in range(N):
    A.append(str(input()))

for i in  range(N):
    B.append(str(input()))

print(A, B)

def _1080(A, B):
    cA = str()
    cB = str()     
    print(A)
    global max_r
    for i in range(M-2):
        r = -2
        for j in range(N):
            x = A[j][i:i+3]
            y = B[j][i:i+3]
            for k in range(3):
                if(x[k] != y[k] and [i,j] not in pre_v):
                    r += 1
        if(r >= max_r and [i,j] not in pre_v):
            max_r = i
            pre_v.append([i,j])

    for i in range(len(A)):
        for j in range(3):
            x = A[i][max_r + j]
            if(x == "0"):
                A[i] = A[i][:max_r + j] + "1" + A[i][max_r + j + 1:]
            else:
                A[i] = A[i][:max_r + j] + "0" + A[i][max_r + j + 1:]
       
    for i in A:
        cA += i
    for j in B:
        cB += j
    if(cA == cB):
        return pre_v
    else:
        _1080(A, B)

x = _1080(A, B)
print(x)
