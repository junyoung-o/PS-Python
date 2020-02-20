T = int(input())
P = []
re = []

def so(P):
    r = 0
    x = 0
    P.sort(reverse = True)

    for i in range(0,len(P)):
        for j in range(i+1,len(P)):
            if(P[j][1] > P[i][1]):
                print("i : {}, j : {}".format(P[i], P[j]))
                r += 1
        print("x : {}, r : {}".format(x, r))
        x = max(x, r)
        r = 0
    print(P)
    return x

for s in range(T):
    N = int(input())
    for i in range(N):
        x, y = map(int, input().split())
        P.append([x, y])
    re.append(so(P))
    P = []

for i in re:
    print(i)