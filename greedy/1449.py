N, L = list(map(int, input().split()))
locate = list(map(int, input().split()))
locate.sort()
result = 1

min_n = locate[0]

for i in range(N):
    x = locate[i]
    if(x > min_n - 0.5 + L):
        # print("x : {}".format(x))
        result += 1
        min_n = x

print(result)