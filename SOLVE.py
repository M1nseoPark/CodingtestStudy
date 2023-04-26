def remove(m, n, board):
    removed = set()
    board[0] = list(board[0])
    
    for i in range(1, m):
        board[i] = list(board[i])
        for j in range(1, n):
            if board[i-1][j-1] == board[i-1][j] == board[i][j-1] == board[i][j]:
                removed.add((i-1, j-1)); removed.add((i-1, j))
                removed.add((i, j-1)); removed.add((i, j))
    
    return removed
                
    
def solution(m, n, board):
    answer = 0
    
    while True:
        removed = remove(m, n, board)
        if len(removed) == 0:
            break
        
        answer += len(removed)
        for i, j in removed:
            board[i][j] = 'O'
        
        for j in range(n):
            for i in range(1, m):
                if board[i][j] == 'O':
                    board[i][j], board[i-1][j] = board[i-1][j], board[i][j]
    
        for i in range(m):
            print(board[i])
        print(len(removed))
            
    return answer

#solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"])
        
