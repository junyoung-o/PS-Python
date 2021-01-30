N = int(input())
Se = []

for i in range(N):
    start, end = map(int, input().split())
    Se.append([start, end])

Se.sort(key = lambda x : (x[1],x[0]))

def solve(job):
    start_time = 0
    re = 0

    for i in job:
        if(i[0] >= start_time):
            print(i)
            re += 1
            start_time = i[1]
    return re

print(solve(Se))