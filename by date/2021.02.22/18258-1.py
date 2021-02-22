import sys

class Queue():
    def __init__(self):
        self.q = [0] *  2000001
        self.front = 0
        self.rear = 0

    def is_empty(self):
        if(self.front == self.rear):
            return True
        return False

    def push(self, new):
        self.q[self.rear] = new
        self.rear += 1

    def pop(self):
        if(self.is_empty()):
            return -1
        self.front += 1
        return self.q[self.front - 1]

    def get_size(self):
        return self.rear - self.front

    def get_front(self):
        if(self.is_empty()):
            return -1
        return self.q[self.front]

    def get_back(self):
        if(self.is_empty()):
            return -1
        return self.q[self.rear - 1]


n = int(input())
queue = Queue()

for _ in range(n):
    request = sys.stdin.readline().split()

    if(len(request) == 2):
        queue.push(request[1])

    else:
        if(request[0] == "front"):
            print(queue.get_front())
        
        elif(request[0] == "back"):
            print(queue.get_back())

        elif(request[0] == "pop"):
            print(queue.pop())

        elif(request[0] == "size"):
            print(queue.get_size())

        else:
            print(int(queue.is_empty()))