import sys
input = sys.stdin.readline

n = int(input())
blue = 0
white = 0
paper = []

def set_paper():
    global paper
    for _ in range(n):
        paper.append(list(map(int, input().split())))

def init():
    set_paper()
    return

def get_sum(hs, he, ws, we):
    test = 0
    for i in range(hs, he + 1):
        test += sum(paper[i][ws: we +1])
    return test

def calc_size2(hs, he, ws, we):
    global white, blue, paper
    test = get_sum(hs, he, ws, we)

    if(test == 0):
        white += 1
    elif(test == 4):
        blue += 1
    else:
        white += 4 - test
        blue += test

def is_same(hs, he, ws, we, size):
    global white, blue, paper

    if(size == 1):
        if(paper[hs][ws] == 0):
            white += 1
            return
        else:
            blue += 1
            return

    # if(size == 2):
    #     calc_size2(hs, he, ws, we)
    #     return

    test = get_sum(hs, he, ws, we)

    if(test == 0):
        white += 1
        return

    elif(test == size**2):
        blue += 1
        return

    else:
        ## i
        is_same(hs, (hs + he)//2, ws, (ws + we)//2, size//2)

        ## ii
        is_same(hs, (hs + he)//2, (ws + we)//2 + 1, we, size//2)

        ## iii
        is_same((hs + he)//2 + 1, he, ws, (ws + we)//2, size//2)

        ### iv
        is_same((hs + he)//2 + 1, he, (ws + we)//2 + 1, we, size//2)

def print_result():
    print(white)
    print(blue)

def main():
    is_same(0, n-1, 0, n-1, n)
    print_result()
    return

if(__name__== "__main__"):
    init()
    main()