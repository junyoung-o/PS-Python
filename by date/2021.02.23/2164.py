import queue
import time

start = time.time()
n = int(input())
q = queue.Queue()

if(n % 2 != 0):
    q.put(n)

for i in range(2, n+1, 2):
    num = (n + 3) - i
    q.put(i)

while(q.qsize() != 1):
    q.get()
    q.put(q.get())

print(q.get())
finish = time.time()
print(finish - start)
