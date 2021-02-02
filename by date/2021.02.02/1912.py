N = int(input())
sequence = []
memo = []

def set_sequence():
    global sequence
    
    import sys

    sequence = list(map(int, sys.stdin.readline().split()))

def set_memo():
    memo.append(sequence[0])

def init():
    set_sequence()
    set_memo()

def is_extra():
    check = True
    for x in sequence:
        if(x > 0):
            check = False
            break

    if(check):
        print(max(sequence))

    return check

def record():
    for ind in range(1, N):
        if(sequence[ind] < 0):
            memo.append(max(0, memo[ind - 1] + sequence[ind]))

        else:
            memo.append(memo[ind - 1] + sequence[ind])

def print_result():
    print(max(memo))

def main():
    if(not is_extra()):
        record()
        print_result()

    return
    
if(__name__ == "__main__"):
    init()
    main()