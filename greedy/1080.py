N, M =map(int,input().split())

A = [list(map(int,list(input()))) for _ in range(N)]
B = [list(map(int,list(input()))) for _ in range(N)]

r = 0

def check():
    for i in range(N):
        for j in range(M):
            if(A[i][j] != B[i][j]):
                return 0
    return 1
    
def chage(i, j):
    for t in range(i,i+3):
        for k in range(j,j+3):
            A[t][k] = 1 - A[t][k]

def start():
    global r
    for i in range(0,N-2):
        for j in range(0,M-2):
            if(A[i][j] != B[i][j]):
                chage(i, j)
                r += 1

start()

if check():
    print(r)

else:
    print(-1)