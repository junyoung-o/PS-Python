A, B = list(map(str, input().split()))

x = len(A)
y = len(B)

s = B.find(A[0])
e = B.find(A[x-1])

if(s == -1 and e == -1):
    # A = B[:y-x] + A
    print(y-x)
elif(s == -1 and e != -1):
    temp = B[e]
    in_b = A.index(temp)
    A = A + B[e+1:]
    A = B[0:e - in_b] + A
elif(s != -1 and e == -1):
    temp = x
    A = B[:s] + A
    A = A + B[s+temp:]
elif(s > e):
    temp = x
    A = B[:s] + A
    A = A + B[s+temp:]
elif(e > s):
    temp = B[e]
    in_b = A.index(temp)
    A = A + B[e+1:]
    A = B[0:e - in_b] + A
# print("A : {}, B : {}, s : {}, e : {}".format(A, B, s, e))

i = 0
r = 0
while(i < y):
    if(A[i] != B[i]):
        r += 1
    i += 1

print(r)