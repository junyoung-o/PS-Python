t = int(input())
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
        self.size += 1

    def pop(self):
        if(self.is_empty()):
            return -1
        self.size -= 1
        return self.s.pop()

def define_stack():
    global stack
    stack = Stack()

def init():
    define_stack()
    return

def is_VPS(target):
    if(target == "("):
        stack.push(")")
        return True

    else:
        if(stack.pop() == ")"):
            return True

        if(stack.pop() == -1):
            return False

def main():
    import sys

    for _ in range(t):
        init()
        result = "YES"
        test_str = sys.stdin.readline()
        for target in test_str[:-1]:
            if(not is_VPS(target)):
                result = "NO"
                break
        
        if(stack.size != 0):
            result = "NO"

        print(result)
        
    return

if(__name__=="__main__"):
    main()