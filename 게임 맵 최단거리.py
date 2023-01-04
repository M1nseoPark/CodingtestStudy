from collections import deque

def solution(maps):
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    
    n = len(maps)
    m = len(maps[0])
    
    def bfs():
        q = deque()
        q.append([0, 0])
        visited = [[-1] * m for _ in range(n)]
        visited[0][0] = 0
        
        while q:
            y, x = q.popleft()
            
            if y == n - 1 and x == m - 1:
                return visited[y][x] + 1
            
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= ny < n and 0 <= nx < m and visited[ny][nx] == -1 and maps[ny][nx] == 1:
                    visited[ny][nx] = visited[y][x] + 1
                    q.append([ny, nx])
        
        return -1
                    
    return bfs()
