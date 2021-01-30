n = int(input())

def times(a):
    if(a == 1):
        return 1
    if(a == 2):
        return 3
    if(a == 3):
        return 7
    if(a == 4):
        return 15

    return 1 + 2 * times(a-1)

def inver(h2):
    h3 = [0 for i in range(len(h2))]
    for i in range(len(h2)):
        a, b = h2[i]
        h3[len(h2)- i - 1] = [b,a]
    return h3

def hard(a):
    if(a == 1):
        return [[1, 3]]

    if(a == 2):
        return [[1,2],[1,3],[2,3]]

    if(a == 3):
        h = hard2(a)
        return h

    h1 = hard(a-2)
    h2 = hard(a-3)
    h2 = inver(h2)

    return h1 + [[1,2]] + h2 + [[3,2]] + h1 + [[2,1]] + h2 + [[2,3]] + h1

def hard2(a):
    if(a == 1):
        return [[1, 3]]

    h1 = hard(a-2)

    return h1 + [[1,2], [3,2]] + h1 +[[2,1], [2,3]] + h1

def level(a):
    if(a == 1):
        h1 = hard(a)
        return h1
    if(a == 2):
        h2 = hard(a)
        return h2
    if(a == 3):
        h = hard2(a)
        return h
    if(a > 3):
        h = hard(a)
        return h

t = times(n)
print(t)
h = level(n)
for i in h:
    a, b = i
    print("{} {}".format(a,b))
