import sys

n, m = list(map(int, sys.stdin.readline().split()))
arr = {}
arr2 = {}
qu = []
for i in range(1, n+1):
    x = sys.stdin.readline().rstrip()
    arr[i] = x
    arr2[x] = i

for _ in range(m):
    x = sys.stdin.readline().rstrip()
    qu.append(x)

for x in qu:
    if(("a" <= x[0] and x[0] <= "z") or ("A" <= x[0] and x[0] <= "Z")):
        print(arr2[x])
    else:
        print(arr[int(x)])