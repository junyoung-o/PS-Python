import time

start = time.time()
n = int(input())

class CQueue():
    def __init__(self):
        self.front = 0
        self.rear = 0
        self.q = [-1] * int(n / 2 + 0.5)

    def is_empty(self):
        if(self.rear == self.front):
            return True
        return False

    def push(self, target):
        self.q[self.rear] = target
        self.rear += 1

    def pop(self):
        if(self.is_empty()):
            return -1
        self.front += 1
        return self.q[self.front - 1]

    def get_size(self):
        return len(self.q)

    def pop_point(self, point):
        del self.q[point]

q = CQueue()

for i in range(2, n+1, 2):
    num = (n + 3) - i
    q.push(i)
    
if(n % 2 != 0):
    q.push(n)

point = 0
while(q.get_size() != 1):
    q.pop_point(point)
    point += 1

    if(point >= q.get_size()):
        point = 0

print(q.q[0])
finish = time.time()
print(finish - start)

