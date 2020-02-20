inS = input()

sp = inS.split('-')
pnum = []
mnum = []
p = 0
m = 0
check = False
check1 = False
leng = len(sp)

if("+" in sp[0]):
    x = sp[0].split("+")
    pnum.append(int(x[0])+int(x[1]))
    sp = sp[1:]
    check = True

elif(leng > 2 and ("+" in sp[-2])):
    mnum.append(int(sp[-1]))
    sp = sp[:-1]

elif(leng == 2 and (len(sp[0].split("+")) == 1) and ((len(sp[1].split("+")) == 1))):
    mnum.append(int(sp[0])+int(sp[1]))
    check1 = True

for i in sp:
    if("+" in i):
        t = i.split("+")
        n = int(t[0]) + int(t[1])
        mnum.append(n)
    else:
        if(check == False and check1 == False):
            pnum.append(int(i))
        elif(check1 == True):
            continue
        else:
            mnum.append(int(i))

for i in range(len(pnum)):
    p += pnum[i]

for i in range(len(mnum)):
    m += mnum[i]

result = p - m
print("inS : {}, sp : {}, pnum : {}, p : {}, mnum : {}, m : {}, result : {}".format(inS, sp, pnum, p, mnum, m, result))
#print(result)