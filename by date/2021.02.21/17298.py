n = int(input())
A = list(map(int, input().split()))
stack = None

class Stack():
    def __init__(self):
        self.s = A.copy()
        self.size = len(A)
        self.max = None
        self.right = None
        self.result = [-1] * n

    def is_empty(self):
        if(self.size == 0):
            return True
        return False

    def pop(self):
        if(self.is_empty()):
            return -1
        self.size -= 1
        return self.s.pop()

    def update_result(self, ind, v):
        self.result[ind] = v

    def end_result(self, target, ind):
        if(A[self.result[ind]] > target):
            return self.result[ind]

        if(ind >= n - 1):
            return -1

        return self.end_result(target, self.result[ind])

    def print_result(self):
        for r in self.result[:-1]:
            if(r == -1):
                print(-1, end = " ")
            else:
                print(A[r], end = " ")

        print(-1)


def define_stack():
    global stack
    stack = Stack()

def init():    
    define_stack()
    return

def NGE(ind):
    target = stack.pop()
    
    if(target < A[ind + 1]):
        stack.update_result(ind, ind + 1)

    elif(target < A[stack.result[ind+1]]):
        stack.update_result(ind, stack.result[ind+1])

    else:
        new_v = stack.end_result(target, ind+1)
        stack.update_result(ind, new_v)


def set_result():
    stack.pop()
    stack.result[n - 1] = n - 1

    for ind in range(n - 1):
        backward = n - 2 - ind
        NGE(backward)

def print_result():
    stack.print_result()

def main():
    set_result()
    print_result()
    return

if(__name__=="__main__"):
    init()
    main()