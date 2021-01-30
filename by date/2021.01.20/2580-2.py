table = [10 for i in range(82)]
zero_list = []

def input_table():
    for i in range(9):
        x = list(map(int , input().split()))
        for j in range(9):
            table[i*9 + j + 1] = x[j]

def count_zero():
    cnt = table.count(0)
    if(cnt == 0):
        return True
    else:
        return False

def get_zeros():
    global zero_list

    for i in range(1, 82):
        if(table[i] == 0):
            zero_list.append(i)

def print_result():
    for x in range(9):
        for y in range(9):
            print(table[x * 9 + y + 1], end=" ")
        print()

def checking(loc):
    global table

    if(table[loc] != 0):
        return

    check = [False for x in range(10)]
    check[0] = True

    ## 가로비교
    ran_min = ((loc - 1) // 9) * 9 + 1
    for i in range(ran_min, ran_min + 9):
        # if(table[i]):
        check[table[i]] = True

    ## 세로비교
    ran_min = (loc - 1) % 9 + 1
    for i in range(ran_min, 82, 9):
        # if(table[i]):
        check[table[i]] = True

    ## 9칸 비교
    ran_min = ((((loc - 1) // 9) // 3) * 3) * 9 + (((loc - 1)% 9) // 3) * 3 + 1

    for i in range(ran_min, ran_min+3):
        # if(table[i]):
        check[table[i]] = True

    for i in range(ran_min + 9, ran_min+12):
        # if(table[i]):
        check[table[i]] = True

    for i in range(ran_min + 18, ran_min+21):
        # if(table[i]):
        check[table[i]] = True

    promise = []
    for c in range(1, 10):
        if(not check[c]):
            promise.append(c)

    return promise

def fill(ind):
    global table, zero_list

    if(count_zero()):
        # print()
        print_result()
        exit(0)
        return

    loc = zero_list[ind]

    promise = checking(loc)

    for n in promise:
        table[loc] = n
        fill(ind + 1)
        table[loc] = 0

def main():
    fill(0)

if(__name__ == "__main__"):
    input_table()
    get_zeros()
    main()