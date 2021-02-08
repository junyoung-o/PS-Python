import sys

t = int(input())
clothes = {}
sequence = []

def set_clothes(n):
    global clothes

    clothes = {}

    for _ in range(n):
        _, category = list(map(str, sys.stdin.readline().split()))
        
        if(category in clothes.keys()):
            clothes[category] += 1
        else:
            clothes[category] = 1

def set_sequence():
    global sequence
    sequence = []

def init(n):
    set_clothes(n)
    set_sequence()
    return

def get_result():
    result = 0

    keys = list(clothes.keys())

    sequence.append(clothes[keys[0]])
    result += sequence[0]

    for ind in range(1, len(keys)):
        accumultion = sum(sequence[:ind]) + 1
        result += accumultion * clothes[keys[ind]]
        sequence.append(result)

    return result

def is_extra(n):
    if(n == 0):
        print(0)
        return True
    return False

def main():
    for _ in range(t):
        n = int(input())
        if(not is_extra(n)):
            init(n)
            print(get_result())
    return

if(__name__=="__main__"):
    main()
