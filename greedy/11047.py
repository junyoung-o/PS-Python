inP = list(map(int, input().split()))

N = inP[0]
K = inP[1]
arr = []
result = 0
num = K

for i in range(N):
    arr.append(int(input()))

index = 0
while( index <= N-1  and arr[index] < num): ##
    index += 1
    print(index)

index -= 1
while(index >= 0):
    if(arr[index] < num):
        coin = num // arr[index]
        num -= arr[index] * coin
        result += coin
        index -= 1
    else:
        index -= 1

print(result)