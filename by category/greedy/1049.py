N, M = map(int, input().split())
arr = []

for i in range(M):
    x, y = map(int, input().split())
    arr.append([x,y])
    
arr.sort(key = lambda x : x[0])
arr1 = []

for i in arr:
    arr1.append(i)
arr.sort(key = lambda x : x[1])
arr2 = arr

# 낱개로만
r3 = N * arr2[0][1]

#세트로만
r2 = (N // 6 + 1) * arr1[0][0]

#낱개 + 세트
r1 = (N // 6) * arr1[0][0] + (N % 6) * arr2[0][1]

price = min(r1, r2, r3)

print(price)
# print("r1 : {}, r2 : {}, r3 : {}, price : {}".format(r1, r2, r3, price))