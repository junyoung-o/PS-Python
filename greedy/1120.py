A = str(input())
B = str(input())

def g(A, B):
    x = len(A)
    y = len(B)

    d = y - x

    if(d == 0):
        r = 0
        x -= 1
        while(x > -1):
            if(A[x] != B[x]):
                r += 1
            x -= 1
        print("A : {}, B : {}, d : {}, x : {}, r : {}".format(A, B, d, x, r))
        return r
    
    i1 = B.find(A[0])
    i2 = B.find(A[x-1])
    print("A : {}, B : {}, d : {}, i1 : {}, i2 : {}\n".format(A, B, d, i1, i2))

    if(i1 >= i2 and i1 > 0 and i2 == -1):
        A = B[i1-1] + A
        g(A, B)
    elif(i1 == i2 and i2 != y):
        A = A + B[i1+1]
        g(A, B)
    elif(i2 > i1):
        A = A + B[i2+1]
        g(A, B)
        
re = g(A, B)
print(re)