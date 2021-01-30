N = int(input())
stairs = []
memo = []

def set_stairs():
    import sys

    for _ in range(N):
        x = int(sys.stdin.readline().rstrip("\n"))
        stairs.append(x)

def main():
    memo.append(stairs[0])

    if(N >= 2):
        memo.append(max(stairs[0] + stairs[1], stairs[1]))
        
    if(N >= 3):
        memo.append(max(stairs[0] + stairs[2], stairs[1] + stairs[2]))

    if(N >= 4):
        for step in range(3, N):
            memo.append(max(memo[step - 1] + stairs[step], memo[step - 2] + stairs[step]))
            # memo.append(max(memo[step - 3] + stairs[step - 1] + stairs[step], memo[step - 2] + stairs[step]))

    # print(memo.pop())
    print(memo)

if(__name__ == "__main__"):
    set_stairs()
    main()