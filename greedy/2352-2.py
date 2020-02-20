n = int(input())
pot = list(map(int, input().split()))

for i in range(n):
    pot[i] = [i+1, pot[i]]

lines = [i+1 for i in range(n)]
c = []
select = []

def link(c):
    for i in c:
        ch = True
        x = pot[i[0]-1]
        for j in select:
            if((x[0] < j[0] and x[1] > j[1]) or (x[1] < j[1] and x[0] > j[0])):
                ch = False
        if(ch):
            select.append(x)

def _2352(a):
    for i in a:
        r = 0
        x = pot[i-1]
        for j in (pot[i-1][1], n):
            y = pot[j-1]
            if((x[0] < y[0] and x[1] > y[1]) or (x[0] > y[0] and x[1] < y[1])):
                 r += 1
        c.append([i, r])

pot.sort(key = lambda x : x[1])
_2352(lines)
print(lines, pot)
c.sort(key = lambda x : x[1])

select.append(pot[c[0][0]-1])
link(c)

print(len(select)-1)