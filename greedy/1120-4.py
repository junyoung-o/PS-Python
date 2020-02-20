A, B = list(map(str, input().split()))

x = -1

for i in A:
    t = B.find(i)
    if(t != -1):
        x = t

if(x == -1):
    len(B) - len(A)

print(x)