N = int(input())
stairs = []
result = 0

def set_stairs():
    global stairs
    import sys

    for _ in range(N):
        x = int(sys.stdin.readline().rstrip("\n"))
        stairs.append(x)

def backward(current, visit):
    global result

    if(current < 0):
        return
    
    visit += 1
    print("Visit : ", stairs[current], current, visit, result)

    if(current == 0):
        if(visit == 3):
            return
        else:
            result = result + stairs[0]
            return

    step_1 = current - 1
    step_2 = current - 2

    if(visit == 3):
        backward(step_2, visit = 0)
        return

    result += stairs[current]

    if(current == 1):
        backward(0, visit)
        return

    if(stairs[step_1] >= stairs[step_2]):
        backward(step_1, visit)
        return

    else:
        if(step_2 - 1 >= 0 and stairs[step_2-1] > stairs[step_2] and visit != 2):
            backward(step_1, visit)
            return
        else:
            backward(step_2, visit = 0)
            return


def main():
    backward(N - 1, 0)
    return
    
if(__name__ == "__main__"):
    set_stairs()
    main()

    print(result)
    