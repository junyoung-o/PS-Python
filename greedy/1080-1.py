N, M = list(map(int, input().split()))
A = []
B = []

for i in range(N):
    A.append(str(input()))

for i in range(N):
    B.append(str(input()))

for j in range(M-3):
    for i in range(N):
        for k in range(3):
            if(A[i][j:j+k] != B[i][j:j+k]):
                if(A[i][j+k] == "0"):
                    A[i] = A[i][:j+k] + "1" + A[i][j+k+1:]
                else:
                    A[i] = A[i][:j+k] + "0" + A[i][j+k+1:]
print(A)

