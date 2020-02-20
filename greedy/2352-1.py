n = int(input())
pot = list(map(int, input().split()))
max_n = 0

for i in range(n):
    pot[i] = [i+1, pot[i]]

select = [i+1 for i in range(n)]

def _2352(a):
    global max_n
    if(len(a) <= max_n):
        return max_n

    temp = [i for i in a]

    for i in a:
        x = pot[i-1]
        for j in a:
            y = pot[j-1]
            if((x[0] < y[0] and x[1] > y[1]) or (x[0] > y[0] and x[1] < y[1])):
                if(x[0] in temp):
                    temp.remove(x[0])
                    r1 = _2352(temp)
                if(y[0] in a):
                    a.remove(y[0])
                    r2 = _2352(a)
                max_n = max(r1, r2)
                return max_n
    print(a)
    return len(a)

print(_2352(select))