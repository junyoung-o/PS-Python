inS = input()

num = []
temp = inS.split("-")
plus = 0
result = 0

for i in temp:
    if('+' in i):
        z = i.split("+")
        num.append(int(z[0]))
        num.append(int(z[1]))
        plus += 1
    else:
        num.append(int(i))

minus = len(num) - (plus + 1)

num.sort()

print("num : {}, plus : {}, minus : {}".format(num, plus, minus))

for i in range(plus+1):
    result += num[i]

for i in range(plus+1, len(num)):
    result -= num[i]

print(result)