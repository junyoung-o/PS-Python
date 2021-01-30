N = int(input())
num = N
P = list(map(int, input().split()))

P.sort()

result = 0

for i in range(0,N):
    result += P[i]*num
    num -= 1

print(result)