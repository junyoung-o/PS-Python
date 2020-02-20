A = str(input())
B = str(input())

x = len(A)
y = len(B)

s = B.find(A[0])
e = B.find(A[x-1])

if(s == -1 and e == -1):
    r = y - x
elif(e > s):
    r = y - A.index(B[e])
elif(s > e):
    r = y - x - 2

print(r)
