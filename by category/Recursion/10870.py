import queue

n = int(input())
q = queue.Queue()

q.put(0)
q.put(1)
cnt = 1
while(cnt <= n):
    x = q.get()
    pre = q.get()
    r = x + pre
    q.put(pre)
    q.put(r)
    cnt += 1

print(q.get())