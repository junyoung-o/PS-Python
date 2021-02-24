from collections import deque
import sys
input = sys.stdin.readline

result = []

n, k = list(map(int, input().split()))
q = deque()

for num in range(1, n+1):
    q.append(num)

while(len(q) != 0):
    for _ in range(k-1):
        q.append(q.popleft())
    result.append(q.popleft())

print("<", end ="")
for r in result[:-1]:
    print(r, end=", ")
print(result[-1], end=">")
