N, M, K = list(map(int, input().split()))
if(N > 1 and M != 0):
    team = int((N+M-K) / 3)
    if(team >= N // 2):
        print(N // 2)
    elif(team >= M):
        print(M)
    else:
        print(team)
else:
    print("0")