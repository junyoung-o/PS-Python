n = int(input())
pot = list(map(int, input().split()))

lines = [[i+1,pot[i]] for i in range(n)]
dur = [[i+1,pot[i]] for i in range(n)]
dur.sort(key = lambda x : x[1])
c = [[i+1] for i in range(n)]
c1 = [[i+1,0] for i in range(n)]
l = [i+1 for i in range(n)]

def link(c1):
    r = 0
    for i in c1:
        if(i[0] in l):
            l.remove(i[0])
            r += 1
            for j in c[i[0]-1]:
                if(j in l):
                    l.remove(j)
    return r

def _2352(a):
    for x in a:
        for j in range(0,x[1]-1):
            y = dur[j]
            if(x[0] < y[0]):
                c[x[0]-1].append(y[0])
                c[y[0]-1].append(x[0])
                c1[x[0]-1][1] += 1
                c1[y[0]-1][1] += 1
                

_2352(lines)
c1.sort(key = lambda x : x[1])
c.sort()
for i in c:
    i[0] = 0
x = link(c1)
# print("c : ", c)
# print("c1 : ", c1)

print(x)