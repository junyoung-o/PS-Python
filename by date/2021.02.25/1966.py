from collections import deque
import sys
input = sys.stdin.readline

t = int(input())
q = None
result = {}
max_priority = -1

def define_queue():
    global q
    q = deque()

def reset_result():
    global result
    result ={}

def set_queue(n):
    document = [i for i in range(n)]
    priority = list(map(int, input().split()))
    for ele in zip(document, priority):
        q.append(ele)

def update_max_priority():
    global max_priority, q
    if(len(q) == 0):
        return
    max_priority = max(list(map(lambda x : x[1], q)))

def init(n):
    define_queue()
    set_queue(n)
    reset_result()
    update_max_priority()

def set_result():
    sequence = 1
    while(len(q) != 0):
        document, priority = q.popleft()
        if(priority == max_priority):
            result[document] = sequence
            sequence += 1
            update_max_priority()

        else:
            q.append([document, priority])

def main():
    for _ in range(t):
        n, m = list(map(int, input().split()))
        init(n)
        set_result()
        print(result[m])

if(__name__== "__main__"):
    main()