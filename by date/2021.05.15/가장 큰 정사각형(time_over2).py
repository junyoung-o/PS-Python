def is_rectangle(board, i, j, window):
    for x in range(i, i+window):
        if(0 in board[x][j:j+window]):
            return False
    return True
    
result = 0
def get_result(board, i, j, window):
    global result
    
    if(i >= len(board) - window + 1 or j >= len(board[0]) - window + 1):
        return

    if(window**2 == result):
        return
       
    if(board[i][j] == 1):
        if(is_rectangle(board, i, j, window)):
            print(window, i, j)
            result = max(window**2, result)
            return
        
    get_result(board, i + 1, j, window)
    get_result(board, i, j + 1, window)
    get_result(board, i + 1, j + 1, window)

def solution(board):
    for window in range(1, min(len(board[0]), len(board)) + 1):
        window = abs(window - min(len(board[0]), len(board))) + 1
        if(result == 0):
            get_result(board, 0, 0, window)
            
    answer = result
    return answer