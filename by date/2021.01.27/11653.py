N = int(input())

temp = N

if(temp != 1):
    for i in range(2, N + 1):
        if(temp < i):
            break

        while(temp % i == 0):
            temp = temp // i
            print(i)

        if(temp == 1):
            break