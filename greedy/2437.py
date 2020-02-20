N = int(input())
gram = list(map(int, input().split()))

gram.sort()
if(N >= 2):
    if(gram[0] == 1):
        if(gram[1] - gram[0] <= 1):
            sum_n = gram[0] + gram[1]
            for i in range(2,N):
                if(sum_n >= gram[i] or (sum_n + 1) == gram[i]):
                    sum_n += gram[i]
                else:
                    break
        else:
            sum_n = gram[0]
    else:
        sum_n = 0
    print(sum_n + 1)

else:
    if(gram[0] == 1):
        print(gram[0]+1)
    else:
        print(1)