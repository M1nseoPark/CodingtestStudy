def solution(board):
    answer = 0
    n = len(board)
    m = len(board[0])
    
    for i in range(n):
        for j in range(m):
            if i > 0 and j > 0 and board[i][j] == 1:
                board[i][j] += min(board[i-1][j-1], board[i-1][j], board[i][j-1])
            answer = max(answer, board[i][j])
    
    return answer ** 2