from collections import deque
import sys

n = int(sys.stdin.readline())
q = deque()

if(n % 2 != 0):
    q.append(n)

for i in range(2, n+1, 2):
    num = (n + 3) - i
    q.append(i)

while(len(q) != 1):
    q.popleft()
    q.append(q.popleft())

print(q.popleft())
