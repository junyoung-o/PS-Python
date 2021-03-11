import sys
input = sys.stdin.readline

n = int(input())
paper = []

## [-1, 0, 1]
result = {-1: 0,
          0 : 0,
          1 : 0}

for _ in range(n):
    paper.append(list(map(int, input().split())))

def counting(h, w, size):
    cnt = {-1:0,
            0:0,
            1:0}
    for i in range(h[0], h[1] + 1):
        cnt[-1] += paper[i][w[0]:w[1] + 1].count(-1)
        cnt[0] += paper[i][w[0]:w[1] + 1].count(0)
        cnt[1] += (size - cnt[-1] - cnt[0])
    return cnt

def is_extra(h, w, size):
    if(size == 1):
        result[paper[h[0]][w[0]]] += 1
        return True

    cnt = counting(h, w, size)
    
    if(cnt[-1] == size**2):
        result[-1] += 1
        return True

    elif(cnt[0] == size**2):
        result[0] += 1
        return True

    elif(cnt[1] == size**2):
        result[1] += 1
        return True

    return False

def div_nine(h, w, size):
    if(is_extra(h, w, size)):
        return

    hs, he = h
    ws, we = w

    length = size // 3

    ## 1
    div_nine([hs, hs + length-1], [ws, ws + length - 1], size//3)

    ## 2
    div_nine([hs, hs + length-1], [ws + length, ws + length*2 - 1], size//3)

    ## 3
    div_nine([hs, hs + length-1], [ws + length*2, we], size//3)

    ## 4
    div_nine([hs + length, hs + length * 2 - 1], [ws, ws + length - 1], size//3)

    ## 5
    div_nine([hs + length, hs + length * 2 - 1], [ws + length, ws + length * 2 - 1], size//3)

    ## 6
    div_nine([hs + length, hs + length * 2 - 1], [ws + length * 2, we], size//3)

    ## 7
    div_nine([hs + length * 2, he], [ws, ws + length - 1], size//3)

    ## 8
    div_nine([hs + length * 2, he], [ws + length, ws + length * 2 - 1], size//3)

    ## 9
    div_nine([hs + length * 2, he], [ws + length * 2, we], size//3)

div_nine([0, n-1], [0, n-1], n)
[print(r) for r in result.values()]