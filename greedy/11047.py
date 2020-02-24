inP = list(map(int, input().split()))

N = inP[0]
K = inP[1]
arr = []
result = 0
num = K

for i in range(N):
    arr.append(int(input()))

arr.sort(reverse = True)

index = 0
while(N > index and num > 0):
    if(arr[index] <= num):
        ##print("num : {}, result : {}, index : {}".format(num,result,index))
        coin = num // arr[index]
        num -= arr[index] * coin
        result += coin
        index += 1
        ##print("num : {}, coin : {}, result : {}, index : {}".format(num,coin,result,index))
    else:
        index += 1

print(result)