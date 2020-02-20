n, x, y = list(map(int, input().split()))
a = x
b = y

if(x % 2 != 0):
    a = x - 1
if(y % 2 != 0):
    b = y - 1

m = pow(2, n)

temp = (m * 2) * (a // 2) + 4 * (b // 2)
# print(temp)
d1 = x - a
d2 = y - b

if(d1 + d2 == 2):
    temp += 3

elif(d1 == 1):
    temp += 2

elif(d2 == 1):
    temp += 1

print(temp)