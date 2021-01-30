A, B = list(map(str, input().split()))

x = 0
nn =100

n1 = len(A)
n2 = len(B)

n3 = n2 - n1

for i in range(n3+1):
    for j in range(n1):
        if(A[j] != B[i + j]):
            x += 1
        print("A[j] : {}, B[i+j] : {}, x : {}".format(A[j], B[i+j], x))

    nn = min(nn,x)
    x = 0

print(nn)