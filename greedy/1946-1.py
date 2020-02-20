import sys
N = 10000000
sys.setrecursionlimit(N)

T = int(input())
Person = []
result = [0]

def solve(Person , arr, i):
    r1 = 0
    r2 = 0

    if(len(Person) == i+1):
        # print("Person : {}, arr : {}, i : {}".format(Person, arr, i))
        return len(arr)

    if(arr[-1][1] > Person[i][1]):
        arr.append(Person[i])
        r1 = solve(Person, arr, i+1)
        return max(r1, r2)
    else:
        r2 = solve(Person, arr, i+1)
        return max(r1, r2)

    return max(r1, r2)

for s in range(T):
    N = int(input())
    arr = []
    for i in range(N):
        x, y = map(int, input().split())
        Person.append([x, y])
    Person.sort()
    for i in range(0,len(Person)):
        arr.append(Person[i])
        x = solve(Person, arr, i)
        if(x > result[s]):
            result[s] = x
            # print("x : {}\n".format(x))
        arr = []
    result.append(0)
    Person = []

for i in range(0,T):
    print(result[i])