k = int(input())
stack = None

class Stack():
    def __init__(self):
        self.s = []
        self.size = 0

    def is_empty(self):
        if(self.size == 0):
            return True
        return False

    def push(self, x):
        self.s.append(x)
        self.size  += 1

    def pop(self):
        if(self.is_empty()):
            return False
        self.size -= 1
        return self.s.pop()

    def get_sum(self):
        return sum(self.s)

def define_stack():
    global stack
    stack = Stack()

def set_stack():
    import sys
    for _ in range(k):
        x = int(sys.stdin.readline())

        if(x == 0):
            stack.pop()
        else:
            stack.push(x)

def init():
    define_stack()
    set_stack()
    return

def get_result():
    return stack.get_sum()

def main():
    print(get_result())
    return

if(__name__=="__main__"):
    init()
    main()