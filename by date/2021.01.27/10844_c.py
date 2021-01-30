N = int(input())
memo = [[0 for _ in range(11)] for _ in range(101)]
div = 1000000000

def set_memo():
    for i in range(1, 10):
        memo[1][i] = 1

def main():
    for i in range(2, N + 1):
        memo[i][0] = memo[i-1][1]
        for j in range(1, 10):
            memo[i][j] = (memo[i-1][j-1] + memo[i-1][j+1]) % div

    print(sum(memo[N]) % div)
        
if(__name__ == "__main__"):
    set_memo()
    main()