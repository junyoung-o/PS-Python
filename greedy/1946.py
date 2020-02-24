T = int(input())

for s in range(T):
    N = int(input())
    arr = []
    Person = []
    r = 1

    for i in range(N):
        x, y = map(int, input().split())
        Person.append([x, y])

    Person.sort()
    arr.append(Person[0])

    for p in Person:
        if(arr[-1][1] > p[1]):
            arr.append(p)

    print(len(arr))
    