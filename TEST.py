from collections import deque

def solution(board):
    answer = []
    start = [0, 0]
    n, m = len(board), len(board[0])
    
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    
    for i in range(n):
        for j in range(m):
            if board[i][j] == 'R':
                start = [i, j]
                
    
    q = deque()
    q.append([start[0], start[1], 0])
    print(start)
    
    while q:
        y, x, dist = q.popleft()
        print(y, x, dist)
        
        if board[y][x] == 'G':
            answer.append(dist)
            break
        
        cnt=0
        while True:
            ny = y + dy[1]
            nx = x + dx[1]
            
            if ny < 0 or nx < 0 or ny >= n or nx >= m:
                break
            
            if board[ny][nx] != '.':
                break
            
            y, x = ny, nx
            cnt += 1
        
        q.append([y, x, dist+cnt])
        print(y, x, dist+cnt)
        
        # for i in range(4):
        #     cnt = 0
        #     while True:
        #         ny = y + dy[i]
        #         nx = x + dx[i]
                
        #         if ny < 0 or nx < 0 or ny >= n or nx >= m:
        #             break
                
        #         if board[ny][nx] != '.':
        #             break
                
        #         y, x = ny, nx
        #         cnt += 1
            
        #     q.append([y, x, dist+cnt])
            
            
    return answer

solution(["...D..R", ".D.G...", "....D.D", "D....D.", "..D...."])