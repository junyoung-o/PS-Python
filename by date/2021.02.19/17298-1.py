n = int(input())
result = [-1] * n
A = None

class Stack():
    def __init__(self):
        self.s = []
        self.size = 0

    def is_empty(self):
        if(self.size == 0):
            return True
        return False

    def push_list(self, new_list):
        self.s += new_list
        self.size += len(new_list)

    def push(self, new):
        self.s.append(new)
        self.size += 1

    def pop(self):
        if(self.is_empty()):
            return -1
        self.size -= 1
        return self.s.pop()

def define_A():
    global A
    A = Stack()

def set_A():
    A.push_list(list(map(int, input().split())))    

def init():
    define_A()
    set_A()
    return

def NGE(ind, max_for_compare):
    new_max = max_for_compare

    current = A.pop()
    print(current, new_max)

    if(current > max_for_compare):
        new_max = current
        result[ind] = -1

    else:
        result[ind] = new_max
        new_max = current

    return new_max    

def set_result():
    max_for_compare = -1

    for ind in range(n):
        backward = (n - 1) - ind
        max_for_compare = NGE(backward, max_for_compare)

def print_result():
    [print(r, end=" ") for r in result]

def main():
    set_result()
    print_result()
    return

if(__name__=="__main__"):
    init()
    main()