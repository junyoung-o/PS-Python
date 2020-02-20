n = int(input())
arr = []

mone = 0
zero = 0
one = 0

for i in range(n):
    arr.append(list(map(int, input().split())))

def cal_z(arr):
    sn = 0
    for i in arr:
        sn += i.count(0)
    return sn

def cal_mo(arr):
    sn = 0
    for i in arr:
        sn += i.count(-1)
    return sn

def cal_o(arr):
    sn = 0
    for i in arr:
        sn += i.count(1)
    return sn

def make_a(arr, a, b, c, d):
    temp = []
    for i in range(a,b):
        temp.append(arr[i][c:d])

    return temp

def solve(arr, n):
    global zero
    global one
    global mone
    print("arr : {}, n : {}".format(arr, n))

    if(n == 3):
        temp_z = cal_z(arr)
        temp_mo = cal_mo(arr)
        temp_o = cal_o(arr)

        if(temp_z == 9):
            zero += 1
            return

        elif(temp_mo == 9):
            mone += 1
            return

        elif(temp_o == 9):
            one += 1
            return

        else:
            mone += temp_mo
            one += temp_o
            zero += temp_z
            return
    
    else:
        temp_z = cal_z(arr)
        temp_mo = cal_mo(arr)
        temp_o = cal_o(arr)
        # print("arr : {}, temp_z : {}, temp_mo : {}, temp_o : {}".format(arr, temp_z, temp_mo, temp_o))
        if(temp_z == n*n):
            zero += 1
            return

        if(temp_mo == n*n):
            mone += 1
            return

        if(temp_o == n*n):
            one += 1
            return

        s = n // 3
        s2 = s * 2

        temp = []
        # a
        temp = make_a(arr,0,s,0,s)
        solve(temp, s)
        temp = make_a(arr,0,s,s,s2)
        solve(temp, s)
        temp = make_a(arr,0,s,s2,n)
        solve(temp, s)
        # b
        temp = make_a(arr,s,s2,0,s)
        solve(temp, s)
        temp = make_a(arr,s,s2,s,s2)
        solve(temp, s)
        temp = make_a(arr,s,s2,s2,n)
        solve(temp, s)
            
        # c
        temp = make_a(arr,s2,n,0,s)
        solve(temp, s)
        temp = make_a(arr,s2,n,s,s2)
        solve(temp, s)
        temp = make_a(arr,s2,n,s2,n)
        solve(temp, s)
    return

solve(arr, n)
print("{}\n{}\n{}".format(mone, zero, one))