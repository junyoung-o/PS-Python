n = int(input())
A = list(map(int, input().split()))
stack = None
result = [-1] * n

class Stack():
    def __init__(self):
        self.s = [0]
        self.size = 1

    def is_empty(self):
        if(self.size == 0):
            return True
        return False

    def pop(self):
        if(self.is_empty()):
            return -1
        self.size -= 1
        return self.s.pop()

    def push(self, new):
        self.s.append(new)
        self.size += 1

    def get_compare(self):
        return self.s[-1]

  
def define_stack():
    global stack
    stack = Stack()

def init():    
    define_stack()
    return

def NGE(target):
    while(stack.size > 0):
        compare = stack.get_compare()
        if(A[compare] < A[target]):
            result[stack.pop()] = A[target]
        else:
            break

    stack.push(target)

def set_result():
    for target in range(1, n):
        NGE(target)

def is_extra():
    if(n == 1):
        print(-1)
        return True
    return False

def print_result():
    [print(r, end=" ") for r in result]

def main():
    if(not is_extra()):
        set_result()
        print_result()
    return

if(__name__=="__main__"):
    init()
    main()