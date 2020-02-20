N = int(input())
arr = []
P = []

for i in range(N):
    start, end = map(int, input().split())
    arr.append([start, end])

arr.sort(reverse = True)
arr.sort(key = lambda x : x[1], reverse = True)

for i in range(0, len(arr)-1):
    index = i+1
    while(arr[i][0] < arr[index][1]):
        index += 1
        if(index == N):
            break
    P.append(index)
P.append(N)

def maxj(a, b):
    if(a >= b):
        return a
    else:
        return b

def jobs(job):
    if(job == N-1):
        return 1
    elif(job == N):
        return 0

    return maxj(jobs(job+1), jobs(P[job])+1)

re = jobs(0)

print(re, arr)