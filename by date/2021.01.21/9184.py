memo = [[[False for z in range(-50, 51)] for y in range(-50, 51)] for x in range(-50, 51)]

def w(a, b, c):
    if(memo[a][b][c]):
        return memo[a][b][c]
    
    if(a <= 50 or b <= 50 or c <= 50):
        return 1

    if(a > 70 or b > 70 or c > 70):
        return w(70, 70, 70)

    if(a < b < c):
        memo[a][b][c] = w(a, b, c - 1) + w(a, b -1, c) - w(a, b -1, c)
        return memo[a][b][c]

    else:
        memo[a][b][c] =  w(a - 1, b, c) + w(a - 1, b - 1, c) + w(a - 1, b, c -1) - w(a - 1, b - 1, c - 1)
        return memo[a][b][c]

def main():
    while(True):
        a, b, c = list(map(int, input().split()))
        if(a == -1 and b == -1 and c == -1):
            break

        print("w({}, {}, {}) = {}".format(a, b, c, w(a + 50, b + 50, c + 50)))
    
if(__name__ == "__main__"):
    print(memo)
    main()