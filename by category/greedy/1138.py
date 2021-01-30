N = int(input())
p = list(map(int, input().split()))
S = []
r = str()
K = [[a+1, p[a]] for a in range(N)]

K.sort(key = lambda x : (x[0],x[1]), reverse = True)

for i in K:
    c = len(S)
    if(c <= i[1]):
        S.append(i[0])
    else:
        S = S[:i[1]] + [i[0]] + S[i[1]:]

for i in S:
    r = r + str(i) + " "

print(r.rstrip(" "))