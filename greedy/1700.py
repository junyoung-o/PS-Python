N, K = list(map(int, input().split()))
plug = [[] for _ in range(N)]
use = list(map(int, input().split()))
x = max(use)
c = [use.count(i) for i in range(x+1)]
result = 0
# [번호. 빈도]
my_use = [[i, c[i]] for i in range(x+1)]

for i in range(N):
    plug[i] = my_use[use[i]]

for i in range(N,K):
    plug.sort(key = lambda x : x[1])
    x = my_use[use[i]]
    if(x not in plug):
        print("plug : {}".format(plug))
        plug[0] = x
        print("plug : {}".format(plug))
        result += 1

print(result, plug)