N = int(input())
results = [-1 for i in range(1000001)]

def fibo():
    results[0] = 0
    results[1] = 1
    results[2] = 2

    i = 3
    while(i <= N):
        results[i] = (results[i - 1] + results[i - 2]) % 15746
        i += 1

def main():
    fibo()
    
if(__name__ == "__main__"):
    main()
    print(results[N])