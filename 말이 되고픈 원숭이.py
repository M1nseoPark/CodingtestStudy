from collections import deque

k = int(input())
w, h = map(int, input().split())

board = []
for _ in range(h):
    board.append(list(map(int, input().split())))

dx = [-1, 1, -2, 2, -2, 2, -1, 1, -1, 1, 0, 0]
dy = [-2, -2, -1, -1, 1, 1, 2, 2, 0, 0, -1, 1]

def bfs(y, x):
    q = deque()
    q.append([y, x])
    board[y][x] = 1
    follow = 0

    while q:
        y, x = q.popleft()

        if y == (h - 1) and x == (w - 1):
            return move[y][x]

        if follow < k:
            for i in range(8):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < w and 0 <= ny < h and board[ny][nx] == 0:
                    q.append([ny, nx])
                    board[ny][nx] = 1
                    move[ny][nx] = move[y][x] + 1
                    follow += 1
                        
            
        for i in range(8, 12):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < w and 0 <= ny < h and board[ny][nx] == 0:
                q.append([ny, nx])
                board[ny][nx] = 1
                move[ny][nx] = move[y][x] + 1

    return -1


move = [[0] * w for _ in range(h)]
print(bfs(0, 0))
    
