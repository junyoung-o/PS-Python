def sqrt(n):
    return n ** (1/2)

def get_result(board):
    h, w = len(board), len(board[0])
    
    for i in range(h - 1):
        for j in range(w - 1):
            if(board[i+1][j+1] == 1):
                board[i+1][j+1] = max(board[i+1][j+1], int((sqrt(min(board[i][j], board[i + 1][j], board[i][j + 1])) + 1)**2))
            
    result = 0
    for i in board:
        result = max(result, max(i))
    
    return result

def solution(board):
    answer = get_result(board)
    return answer