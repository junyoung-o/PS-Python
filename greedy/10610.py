N = str(input())
num = []
bo = False

if('0' not in N):
    print("-1")
    bo = True

if(bo == False):
    for i in range(len(N)):
        n = int(N[i])
        num.append(n)

    num.sort(reverse = True)

    ck = 0
    re = str()

    for i in num:
        ck += i

    if(ck % 3 == 0):
        for i in num:
            re += str(i)
        print(re)
    else:
        print("-1")