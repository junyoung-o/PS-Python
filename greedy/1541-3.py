inS = input()

x = inS.split("-")
num = []
pnum = []
re = 0
ch = 0

for i in x:
    s = i.split("+")
    l = len(s)
    if(l > 1 and ch == 0):
        ch += 1
        for j in s:
            pnum.append(int(j))
    elif(l > 1 and ch != 0):
        for j in s:
            num.append(int(j))
    else:
        num.append(int(i))

print("x : {}, pnum : {}, num : {}".format(x, pnum, num))

if("+" in x[0]):
    for i in range(2,len(num)):
        re += num[i]
    re = num[0]+num[1] - re
    for i in pnum:
        re += i

else:
    for i in range(1,len(num)):
        re += num[i]
    re = num[0] - re
    for i in pnum:
        re += i

print(re)
