A, B = map(str, input().split())
x = -1

def cal(A, B):
    l = len(A)
    i = 0
    r = 0
    while(l > i):
        if(A[i] != B[i]):
            r += 1
        i += 1
    return r

def re(temp1, temp2, B):
    r1 = cal(temp1, B)
    r2 = cal(temp2, B)

    print("temp1 : {}, temp2 : {}, r1 : {}, r2 : {}".format(temp1, temp2, r1, r2))
    if(r1 >= r2):
        r = g(temp2, B)
        return r
    else:
        r = g(temp1, B)
        return r

def g(A, B):
    if(len(B) == len(A)):
        r = cal(A, B)
        print("r : {}, A : {}, B :{}".format(r, A, B))
        return r
    
    print("A : {}, B :{}".format(A, B))
    s = B.find(A[0])
    e = B.find(A[-1])
    global x
    for i in A:
        t = B.find(i)
        if(t != -1):
            x = t

    if(x == -1):
        r = len(B) - len(A)
        return r

    if(s == -1 and e == -1 and x != -1):
        temp1 = B[s] + A
        temp2 = A + B[e]
        r = re(temp1, temp2, B)
        return r 

    if(s == 0 and e + 1 == len(B)):
        temp1 = B[s] + A
        temp2 = A + B[e]
        r = re(temp1, temp2, B)
        return r

    if(s != 0 and e + 1 == len(B)):
        temp1 = B[s-1] + A
        temp2 = A + B[e]
        r = re(temp1, temp2, B)
        return r

    if(s == 0 and e + 1 != len(B)):
        temp1 = B[s] + A
        temp2 = A + B[e+1]
        r = re(temp1, temp2, B)
        return r
    
    else:
        temp1 = B[s-1] + A 
        temp2 = A + B[e+1]
        r = re(temp1, temp2, B)
        return r

r = g(A, B)

print(r)