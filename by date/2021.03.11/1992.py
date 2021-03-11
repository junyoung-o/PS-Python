import sys
input = sys.stdin.readline

n = int(input())
video = []
result = ""

def str_to_list(str_):
    return list(map(int, [i for i in str_]))

def set_video():
    for _ in range(n):
        video.append(str_to_list(input().rstrip()))

def init():
    set_video()
    return

def is_extra(h, w, size):
    global result, video
    hs, he = h
    ws, we = w

    check = 0
    for i in range(hs, he+1):
        check += sum(video[i][ws:we+1])

    if(check == 0):
        result += str(0)
        return True

    elif(check == size**2):
        result += str(1)
        return True

    else:
        return False

def quad_tree(h, w, size):
    global result, video

    hs, he = h
    ws, we = w

    if(size == 1):
        result += str(video[hs][ws])
        return

    if(is_extra(h, w, size)):
        return
    
    else:
        result += "("

        ## 1사분면
        quad_tree([hs, (hs+he)//2], [ws, (ws+we)//2], size//2)

        ## 2사분면
        quad_tree([hs, (hs+he)//2], [(ws+we)//2 + 1, we], size//2)

        ## 3사분면
        quad_tree([(hs+he)//2 + 1, he], [ws, (ws+we)//2], size//2)

        ## 4사분면
        quad_tree([(hs+he)//2 + 1, he], [(ws+we)//2 + 1, we], size//2)

        result += ")"

def print_result():
    global result
    print(result)

def main():
    quad_tree([0, n - 1], [0, n - 1], n)
    print_result()
    return

if(__name__== "__main__"):
    init()
    main()