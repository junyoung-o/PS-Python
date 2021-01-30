N = int(input())
results = [-1 for i in range(1000001)]

def init_results():
    results[0] = -1
    results[1] = 1
    results[2] = 1
    results[3] = 1
    results[4] = 2
    results[5] = 2

def padoban(x):
    i = 6
    while(i <= x):
        results[i] = results[i - 2] + results[i - 3]
        i += 1

def main():
    for _ in range(N):
        x = int(input())
        padoban(x)
        print(results[x])
    
if(__name__ == "__main__"):
    init_results()
    main()