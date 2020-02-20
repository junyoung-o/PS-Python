n = int(input())
link = list(map(int, input().split()))
l = []

for i in range(n):
    l.append(i+1)

for i in range(n):
    link[i] = [i+1,link[i]]

def st():
    min_n = len(l)
    for i in l:
        x = link[i-1]
        r = 0
        s = []
        for j in l:
            y = link[j-1]
            if(x[0] < y[0] and x[1] > y[1]):
                r += 1
                s.append(y)
            elif(x[0] > y[0] and x[1] < y[1]):
                r += 1
                s.append(y)
        if(min_n > r):
            min_n = r
        if(len(s) == 0):
            return len(l)
    for i in s:
        print(i)
        l.remove(i[0])
    st()
    return len(l)

print(n, link)
print(st())