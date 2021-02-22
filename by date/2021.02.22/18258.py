n = int(input())
queue = None

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

def define_queue():
    global queue
    queue = Queue()

def init():
    define_queue()
    return

def get_request():
    import sys
    request = list(map(str, sys.stdin.readline().split()))
    if(len(request) == 2):
        queue.push(request[1])
        return "Complete"
    return request[0]

def perform(request):
    if(request == "front"):
        print(queue.get_front())
    
    elif(request == "back"):
        print(queue.get_back())

    elif(request == "pop"):
        print(queue.pop())

    elif(request == "size"):
        print(queue.get_size())

    elif(request == "empty"):
        print(int(queue.is_empty()))

def main():
    for _ in range(n):
        request = get_request()
        perform(request)

    return

if(__name__=="__main__"):
    init()
    main()