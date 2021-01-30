table = [[] for i in range(9)]
cnt = 0

def input_table():
    global cnt

    for i in range(9):
        x = list(map(int , input().split()))
        table[i] = x
        cnt += x.count(0)

def print_result():
    for x in range(9):
        for y in range(9):
            print(table[x][y], end=" ")
        print()

def check_row(i, j):
    global cnt
    
    if(table[i][j] != 0):
        return
        
    ## 가로비교
    check = [False for x in range(10)]
    for row in range(9):
        if(table[i][row] != 0):
            check[table[i][row]] = True

    for c in range(1, 10):
        if(not check[c] and sum(check) == 8):
            table[i][j] = c
            cnt -= 1
            return

def check_col(i, j):
    global cnt
    if(table[i][j] != 0):
        return
        
    ## 세로비교
    check = [False for x in range(10)]
    for col in range(9):
        if(table[col][j] != 0):
            check[table[col][j]] = True

    for c in range(1, 10):
        if(not check[c] and sum(check) == 8):
            table[i][j] = c
            cnt -= 1
            return

def check_box(i, j):
    global cnt
    if(table[i][j] != 0):
        return
        
    ## 9칸 비교
    check = [False for x in range(10)]

    row_min = (i // 3) * 3
    row_max = row_min + 3

    col_min = (j // 3) * 3
    col_max = col_min + 3

    for row9 in range(row_min, row_max):
        for col9 in range(col_min, col_max):
            if(table[row9][col9] != 0):
                check[table[row9][col9]] = True

    for c in range(1, 10):
        if(not check[c] and sum(check) == 8):
            table[i][j] = c
            cnt -= 1
            return

def fill_anything(i, j):
    global cnt
    if(table[i][j] != 0):
        return

    ## 가로비교
    check = [False for x in range(10)]
    for row in range(9):
        if(table[i][row] != 0):
            check[table[i][row]] = True

    for c in range(1, 10):
        if(not check[c]):
            table[i][j] = c
            cnt -= 1
            return

    ## 세로비교
    check = [False for x in range(10)]
    for col in range(9):
        if(table[col][j] != 0):
            check[table[col][j]] = True

    for c in range(1, 10):
        if(not check[c]):
            table[i][j] = c
            cnt -= 1
            return

    ## 9칸 비교
    check = [False for x in range(10)]

    row_min = (i // 3) * 3
    row_max = row_min + 3

    col_min = (j // 3) * 3
    col_max = col_min + 3

    for row9 in range(row_min, row_max):
        for col9 in range(col_min, col_max):
            if(table[row9][col9] != 0):
                check[table[row9][col9]] = True

    for c in range(1, 10):
        if(not check[c]):
            table[i][j] = c
            cnt -= 1
            return

def fill(i, j):
    global cnt

    if(table[i][j] != 0):
        return

    if(cnt == 0):
        fill_anything(i, j)
        return

    check_row(i, j)
    check_col(i, j)
    check_box(i, j)


def main():
    while(cnt != 0):
        for i in range(9):
            for j in range(9):
                if(table[i][j] == 0):
                    fill(i, j)
                    # print(cnt, i, j)

    # fill(0, 0)

if(__name__ == "__main__"):
    input_table()
    main()
    # print()
    print_result()