N, M = list(map(int, input().split(" ")))
c = True
A = []
B = []
max_r = 0
pre_v = []
for i in range(N):
    A.append(str(input()))

for i in  range(N):
    B.append(str(input()))

# print(A, B)

def _1080(A, B):
    cA = str()
    cB = str()
    
    re = 0
    for i in A:
        cA += i
    for j in B:
        cB += j
    if(cA == cB):
            return re
    global max_r
    for i in range(M-2):
        r = 0
        for j in range(N):
            x = A[j][i:i+3]
            y = B[j][i:i+3]
            for k in range(3):
                if(x[k] != y[k]):
                    r += 1
        if(r >= max_r):
            max_r = r
            pre_v.append([j-2, i])
    # print(pre_v)
    # for i in range(len(A)):
    #     for j in range(3):
    #         x = A[i][max_r + j]
    #         if(x == "0"):
    #             A[i] = A[i][:max_r + j] + "1" + A[i][max_r + j + 1:]
    #         else:
    #             A[i] = A[i][:max_r + j] + "0" + A[i][max_r + j + 1:]
       
    # for i in A:
    #     cA += i
    # for j in B:
    #     cB += j
    # if(cA == cB):
    #     return pre_v
    # else:
    #     _1080(A, B)
    for i in pre_v:
        cA = str()
        cB = str()
        re += 1
        ia = int(i[0])
        ib = int(i[1])
        for k in range(3):
            for s in range(3):
                # print("K : {}, s: {}".format(k, s))
                x = A[ia+k][ib+s]
                if(x == "0"):
                    # print(A[ia], " -> ",)
                    A[ia+k] = A[ia+k][:ib+s] + "1" + A[ia+k][ib+s+1:]
                    # print(A[ia])
                if(x == "1"):
                    A[ia+k] = A[ia+k][:ib+s] + "0" + A[ia+k][ib+s+1:]

        # print(A)
        for i in A:
            cA += i
        for j in B:
            cB += j
        if(cA == cB):
            return re
        elif(re > 50 or re >= (M//3 + 1)):
            return -1
    return re

if(N >= 3 and M >= 3):
    x = _1080(A, B)
    print(x)
else:
    print(-1)