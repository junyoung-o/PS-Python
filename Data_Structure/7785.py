import sys

n = int(sys.stdin.readline())
log = {}

for _ in range(n):
    x, y = list(map(str, sys.stdin.readline().split()))
    log[x] = y

result = sorted(log.items(),key = lambda x : x[0], reverse = True)

for k, v in result:
    if(v == "enter"):
        print(k)