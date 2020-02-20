N, K = list(map(int, input().split()))
use = list(map(int, input().split()))
plug = [0 for _ in range(N)]

result = 0
ind = 0
jnd = 0
while(jnd >= 0):
    if(jnd >= N):
        jnd = -1
        break

    if(use[ind] not in plug):
        plug[jnd] = use[ind]
        jnd += 1
    ind += 1

# print("plug : {}".format(plug))
for i in range(ind, K):
    c = []
    breaker = False
    if(use[i] not in plug):
        for j in range(N):
            p = plug[j]
            # print(use[i+1:K])
            if(p not in use[i+1:K]):
                plug[j] = use[i]
                result += 1
                # print("1번 plug : {}".format(plug))
                breaker = True
                break

        if(breaker == False):
            for j in range(N):
                p = plug[j]
                c.append(use[i+1:K].index(p))
            m = max(c)
            inm = c.index(m)
            # print("c : ",c,"imn : ", inm)
            plug[inm] = use[i]
            result += 1
            # print("2번 plug : {}".format(plug))

print(result)