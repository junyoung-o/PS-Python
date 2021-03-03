from collections import deque
import sys
input = sys.stdin.readline

q = None

t = int(input())

p = None
n = 0
arr = []

def set_p():
    global p
    p = input()

def set_n():
    global n
    n = int(input())

def is_extra():
    global n, p
    if(n == 0):
        return True
    return False

def set_arr():
    global arr
    arr_list = input()
    arr = list(map(int, arr_list[1:-2].split(",")))
    
def set_queue():
    global arr, q
    q = deque(arr)

def init():
    set_p()
    set_n()
    if(is_extra()):
        return False
    set_arr()
    set_queue()
    return True

def perform_p():
    global p, q
    
    reverse = -1

    for request in p:
        if(request == "R"):
            reverse *= -1

        if(request == "D"):
            try:
                if(reverse == 1):
                    q.pop()
                else:
                    q.popleft()
            except:
                return False

    if(reverse == 1):
        q.reverse()
    
    return True

def print_result():
    if(len(q) == 0):
        print("[]")
        return
    print("[", end="")
    while(len(q) != 1):
        print(q.popleft(), end=",")
    print(q.pop(), end="")
    print("]")

def perform_extra():
    _ = input()
    if("D" in p):
        print("error")
    else:
        print("[]")

def main():
    global t
    for _ in range(t):
        if(init()):
            if(perform_p()):
                print_result()
            else:
                print("error")
        else:
            perform_extra()
    return

if(__name__== "__main__"):
    main()