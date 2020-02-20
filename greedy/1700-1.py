N, K = list(map(int, input().split()))
plug = [[] for _ in range(N)]
use = list(map(int, input().split()))
x = max(use)
c = [use.count(i) for i in range(x+1)]
result = 0
# [번호. 빈도]
my_use = [[i, c[i]] for i in range(x+1)]

check = True
ind = 0
jnd = 0
while(check):
    # print("N : {}, ind : {}, jnd : {},\n my_use : {},\n use : {},\nplug : {}".format(N ,ind, jnd, my_use, use, plug))
    if(ind >= N):
        check = False
        break
    if(my_use[use[jnd]] not in plug):
        plug[ind] = my_use[use[jnd]]
        my_use[use[jnd]][1] -= 1
        ind += 1
    jnd += 1

# print("N : {}, ind : {}, jnd : {},\n my_use : {},\n use : {},\nplug : {}".format(N ,ind, jnd, my_use, use, plug))

for i in range(jnd,K):
    plug.sort(key = lambda x : x[1])
    x = my_use[use[i]]
    if(x not in plug):
        # print("plug : {}".format(plug))
        plug[0] = x
        # print("plug : {}".format(plug))
        result += 1
    my_use[use[i]][1] -= 1

print(result, plug)