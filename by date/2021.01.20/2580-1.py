table = [[] for i in range(9)]
visit = [[False for j in range(9)] for i in range(9)]
cnt = 0
back = False

def input_table():
    global cnt

    for i in range(9):
        x = list(map(int , input().split()))
        table[i] = x
        cnt += x.count(0)

def init_visit():
    for i in range(9):
        for j in range(9):
            visit[i][j] = False

# def count_zero():
#     global table
#     tt = 1
#     for i in range(9):
#         tt += table[i].count(0)

#     return tt

def is_all_visit():
    tt = 0
    for i in range(9):
        tt += visit[i].count(True)

    return tt

def print_result():
    for x in range(9):
        for y in range(9):
            print(table[x][y], end=" ")
        print()

# def check_row(i, j):
#     global cnt, table
    
#     if(table[i][j] != 0):
#         return
        
#     ## 가로비교
#     check = [False for x in range(10)]
#     for row in range(9):
#         if(table[i][row] != 0):
#             check[table[i][row]] = True

#     for c in range(1, 10):
#         if(not check[c] and sum(check) == 8):
#             table[i][j] = c
#             return

# def check_col(i, j):
#     global cnt, table

#     if(table[i][j] != 0):
#         return
        
#     ## 세로비교
#     check = [False for x in range(10)]
#     for col in range(9):
#         if(table[col][j] != 0):
#             check[table[col][j]] = True

#     for c in range(1, 10):
#         if(not check[c] and sum(check) == 8):
#             table[i][j] = c
#             return

# def check_box(i, j):
#     global cnt, table 

#     if(table[i][j] != 0):
#         return
        
#     ## 9칸 비교
#     check = [False for x in range(10)]

#     row_min = (i // 3) * 3
#     row_max = row_min + 3

#     col_min = (j // 3) * 3
#     col_max = col_min + 3

#     for row9 in range(row_min, row_max):
#         for col9 in range(col_min, col_max):
#             if(table[row9][col9] != 0):
#                 check[table[row9][col9]] = True

#     for c in range(1, 10):
#         if(not check[c] and sum(check) == 8):
#             table[i][j] = c
#             return

def fill_anything(i, j):
    global cnt, table

    if(table[i][j] != 0):
        return

    ## 가로비교
    check = [False for x in range(10)]

    for row in range(9):
        if(table[i][row] != 0):
            check[table[i][row]] = True

    ## 세로비교
    for col in range(9):
        if(table[col][j] != 0):
            check[table[col][j]] = True

    ## 9칸 비교
    row_min = (i // 3) * 3
    row_max = row_min + 3

    col_min = (j // 3) * 3
    col_max = col_min + 3

    for row9 in range(row_min, row_max):
        for col9 in range(col_min, col_max):
            if(table[row9][col9] != 0):
                check[table[row9][col9]] = True

    print(check, i ,j)
    for c in range(1, 10):
        if(not check[c]):
            table[i][j] = c
            return

def checking(i, j):
    global cnt, table

    if(table[i][j] != 0):
        return

    ## 가로비교
    check = [False for x in range(10)]

    for row in range(9):
        if(table[i][row] != 0):
            check[table[i][row]] = True

    ## 세로비교
    for col in range(9):
        if(table[col][j] != 0):
            check[table[col][j]] = True

    ## 9칸 비교
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
            return

def fill(i, j):
    global table, cnt, back

    if(table[i][j] != 0):
        return

    if(visit[i][j]):
        return

    if(back):
        cnt -= 1
        print_result()
        print()

    print(cnt, is_all_visit())

    if(is_all_visit() == cnt - 1):
        fill_anything(i, j)
        init_visit()
        visit[i][j] = True
        print_result()
        print()
        cnt -= 1
        back = True
        return

    visit[i][j] = True

    checking(i, j)

    print(i, j)

    for x in range(9):
        for y in range(9):
            if(table[x][y] == 0 and not visit[x][y]):
                fill(x, y)

    return

def main():
    global cnt
    
    while(cnt):
        for i in range(9):
            for j in range(9):
                if(table[i][j] == 0):
                    fill(i, j)
                    break


if(__name__ == "__main__"):
    input_table()
    init_visit()
    main()
    print()
    print_result()