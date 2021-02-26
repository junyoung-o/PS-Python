from collections import deque
import sys
input = sys.stdin.readline

t = int(input())
q = deque()

def is_empty():
    if(len(q) == 0):
        return True
    return False

def main():
    for _ in range(t):
        request = list(map(str,input().split()))
        if(len(request) == 2):
            if(request[0] == "push_back"):
                q.append(request[1])
            else:
                q.appendleft(request[1])

        else:
            r = request[0]
            if(r == "pop_front"):
                if(is_empty()):
                    print(-1)
                else:
                    print(q.popleft())

            elif(r == "pop_back"):
                if(is_empty()):
                    print(-1)
                else:
                    print(q.pop())

            elif(r == "size"):
                print(len(q))

            elif(r == "empty"):
                print(int(is_empty()))

            elif(r == "front"):
                if(is_empty()):
                    print(-1)
                else:
                    print(list(q)[0])
            else:
                if(is_empty()):
                    print(-1)
                else:
                    print(list(q)[-1])
    return

if(__name__== "__main__"):
    main()