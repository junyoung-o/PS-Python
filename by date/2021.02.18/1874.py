from typing import Sequence


n = int(input())
sequence = []
result = None
candidate = None

class Stack():
    def __init__(self):
        self.s = []
        self.size = 0

    def is_empty(self):
        if(self.size == 0):
            return True
        return False

    def push(self, target):
        self.s.append(target)
        self.size += 1

    def pop(self):
        if(self.is_empty()):
            return -1
        self.size -= 1
        return self.s.pop()


def define_stack():
    global result, candidate
    result = Stack()
    candidate = Stack()

def set_sequence():
    global sequence
    
    import sys
    for _ in range(n):
        sequence.append(int(sys.stdin.readline()))

def init():
    define_stack()
    set_sequence()
    return

def get_result():
    point = 0
    result_list = []

    for num in range(1, n+1):
        candidate.push(num)
        result_list.append("+")
        
        if(num == sequence[point]):
            while(True):
                target = candidate.pop()

                if(point < n and target == sequence[point]):
                    result.push(target)
                    result_list.append("-")
                    point += 1

                else:
                    if(target != -1):
                        candidate.push(target)

                    break

    if(candidate.size != 0):
        return "NO"

    return result_list

def print_result(result_list):
    if(result_list == "NO"):
        print(result_list)
    else:
        [print(r, end="\n") for r in result_list]

def main():
    print_result(get_result())
    return

if(__name__=="__main__"):
    init()
    main()