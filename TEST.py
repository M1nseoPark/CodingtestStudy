from collections import deque

def solution(board):
    answer = -1
    
    n, m = len(board), len(board[0])
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    sy, sx, ey, ex = -1, -1, -1, -1
    
    for i in range(n):
        board[i] = list(board[i])
        for j in range(m):
            if board[i][j] == 'R':
                sy, sx = i, j
            elif board[i][j] == 'G':
                ey, ex = i, j
    
    q = deque()
    q.append([sy, sx])
    dict = [[-1] * m for _ in range(n)]
    dict[sy][sx] = 0
    
    while q:
        y, x = q.popleft()
        
        if y == ey and x == ex:
            answer = dict[y][x]
            break
        
        ny, nx = y, x
        for i in range(4):
            while True:
                ny += dy[i]
                nx += dx[i]
                
                if ny < 0 or ny >= n or nx < 0 or nx >= m:
                    print(ny-dy[i], nx-dx[i])
                    if dict[ny-dy[i]][nx-dx[i]] == -1:
                        q.append([ny-dy[i], nx-dx[i]])
                        dict[ny-dy[i]][nx-dx[i]] = dict[y][x] + 1
                    break
                
                if board[ny][nx] == 'D':
                    if dict[ny-dy[i]][nx-dx[i]] == -1:
                        q.append([ny-dy[i], nx-dx[i]])
                        dict[ny-dy[i]][nx-dx[i]] = dict[y][x] + 1
                    break
            
    return answer

solution(["...D..R", ".D.G...", "....D.D", "D....D.", "..D...."])
