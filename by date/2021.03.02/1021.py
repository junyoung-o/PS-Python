from collections import deque
import sys
input = sys.stdin.readline

n, m = list(map(int, input().split()))
extract = list(map(int, input().split()))
q = deque([i for i in range(1, n + 1)])

def move_left():
    q.append(q.popleft())

def move_right():
    q.appendleft(q.pop())

def pop_left():
    q.popleft()

def get_result():
    result = 0
    for ind in extract:
        loc = list(q).index(ind)

        if(loc == 0):
            pop_left()

        elif(loc < len(q) - loc):
            for _ in range(loc):
                move_left()
            pop_left()
            result += loc
        
        else:
            for _ in range(len(q) - loc):
                move_right()
            pop_left()
            result += len(q) - loc + 1

    return result

def main():
    print(get_result())
    return

if(__name__== "__main__"):
    main()