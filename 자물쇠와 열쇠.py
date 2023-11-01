def solution(key, lock):
    m, n = len(key), len(lock)
    board = [[0] * (m*2 + n) for _ in range(m*2+n)]
    for i in range(n):
        for j in range(n):
            board[m+i][m+j] = lock[i][j]

    # 열쇠 시계방향 90도 회전하기 
    def rotate(arr):
        return list(zip(*arr[::-1]))
    
    # 열쇠 넣어보기 
    def attach(y, x, key, board):
        for i in range(m):
            for j in range(m):
                board[x+i][y+j] += key[i][j]
    
    # 열쇠 열 수 있는지 검사 
    def check(board):
        for i in range(n):
            for j in range(n):
                if board[m+i][m+j] != 1:
                    return False
        return True

    # 열쇠 다시 빼기 
    def detach(y, x, key, board):
        for i in range(m):
            for j in range(m):
                board[x+i][y+j] -= key[i][j]

    for _ in range(4):
        key = rotate(key)

        for y in range(1, m+n):
            for x in range(1, m+n):
                attach(y, x, key, board)
                if check(board):
                    return True
                detach(y, x, key, board)

    return False
    

