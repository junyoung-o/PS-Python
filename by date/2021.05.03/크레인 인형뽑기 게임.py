g_board = []
g_moves = []
stack = []
result = 0

def set_board(board):
    global g_board
    g_board = board

def set_moves(moves):
    global g_moves
    g_moves = moves

def set_stack():
    stack.append(-1)
    
def init(board, moves):
    set_board(board)
    set_moves(moves)
    set_stack()

def compare(picked_toy):
    global result
    
    compare_toy = stack.pop()
    
    if(compare_toy == -1):
        stack.append(compare_toy)
        stack.append(picked_toy)
        return

    if(compare_toy == picked_toy):
        result += 2
        return
    
    stack.append(compare_toy)
    stack.append(picked_toy)
    
    
def pick(move):
    global g_board
    
    flag = False
    move = move - 1
    picked = -1
    
    for row in range(len(g_board)):
        if(g_board[row][move] != 0):
            picked = g_board[row][move]
            g_board[row][move] = 0
            flag = True
            break
    
    return picked, flag
    
def set_result(board, moves):       
    for move in g_moves:
        picked_toy, flag = pick(move)
        if(flag):
            compare(picked_toy)
    
def solution(board, moves):
    init(board, moves)
    set_result(board, moves)
    answer = result
    return answer