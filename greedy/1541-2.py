inS = input()

ms = inS.split("-")
ps = inS.split("+")

s = inS.split("-")

pnum = []
mnum = []

c1 = len(ms)
c2 = len(ps)
check = False
check1 = False

if("+" in ms[0]):
    check = True

if("-" in ps[0]):
    check1 = True

if(c1 == 1 and c2 == 1):
    print(inS)

elif(c1 == 1 and c2 != 1):
    print(int(ps[0]) + int(ps[1]))

elif(c1 != 1 and c2 == 1):
    print(int(ms[0]) - int(ms[1]))

else:
    for i in s:
        x = i.split("+")

        if(len(x) == 2):
            if(check == True):
                pnum.append(int(x[0]) + int(x[1]))
                check = False

            elif(check == False):
                mnum.append(int(x[0]) + int(x[1]))

            else:
                pnum.append(int(x[0]) + int(x[1]))

        else:
            if(check1 == True):
                pnum.append(int(i))
                check1 = False
            else:
                mnum.append(int(i))
    p = 0
    m = 0
    re = 0
    for i in pnum:
        p += i
    for i in mnum:
        m -= i
    re = p +m
    print(re)