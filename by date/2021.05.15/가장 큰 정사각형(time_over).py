def is_rectangle(board, i, j, window):
    for x in range(i, i+window):
        if(0 in board[x][j:j+window]):
            return False
    return True

def get_result(board):
    result = 0
    h, w = len(board), len(board[0])
    
    for window in range(1, min(h, w) + 1):
        window = abs(window - min(h, w)) + 1
        for i in range(h - window + 1):
            for j in range(w - window + 1):
                if(is_rectangle(board, i, j, window)):
                    result = max(window**2, result)
                    break
                    
            if(window**2 == result):
                break
                
        if(window**2 == result):
                break
            
    return result

def solution(board):
    answer = get_result(board)
    return answer