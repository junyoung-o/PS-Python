n = int(input())
stack = None

class Stack:
    def __init__(self):
        self.size = 0
        self.s = []

    def is_empty(self):
        if(self.size == 0):
            return True
        else:
            return False

    def pop(self):
        if(self.is_empty()):
            return -1

        self.size -= 1
        return self.s.pop()

    def push(self, x):
        self.s.append(x)
        self.size += 1

    def top(self):
        if(self.is_empty()):
            return -1
        return self.s[-1]


def init():
    global stack
    stack = Stack()
    return

def main():
    import sys
    for _ in range(n):
        requests = list(map(str, sys.stdin.readline().split()))

        request = requests[0]

        if(request == "push"):
            stack.push(int(requests[1]))

        elif(request == "pop"):
            print(stack.pop())

        elif(request == "top"):
            print(stack.top())
    
        elif(request == "size"):
            print(stack.size)

        elif(request == "empty"):
            print(int(stack.is_empty()))

        else:
            raise IOError
    return

if(__name__=="__main__"):
    init()
    main()