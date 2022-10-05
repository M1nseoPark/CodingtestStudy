from collections import deque

def bfs(y, x):
    q = deque()
    q.append([y, x])
    visited = [[0] * c for i in range(l*r)]
    visited[y][x] = 1

    while q:
        y, x = q.popleft()

        if y == finish[0] and x == finish[1]:
            return visited[y][x] - 1

        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < c and 0 <= ny < l*r:
                if maps[ny][nx] != '#' and visited[ny][nx] == 0:
                    q.append([ny, nx])
                    visited[ny][nx] = visited[y][x] + 1

    
    return -1
            
        

while True:
    l, r, c = map(int, input().split())

    if l == 0 and r == 0 and c == 0:
        break

    maps = []
    for _ in range(l*r+l):
        temp = list(input())
        if len(temp) != 0:
            maps.append(temp)
    
    dx = [0, 0, -1, 1, 0, 0]
    dy = [-1, 1, 0, 0, -r, r]
        
    start = [0, 0]
    finish = [0, 0]
    
    for i in range(l*r):
        for j in range(c):
            if maps[i][j] == 'S':
                start[0], start[1] = i, j

            if maps[i][j] == 'E':
                finish[0], finish[1] = i, j

    answer = bfs(start[0], start[1])
    if answer != -1:
        print('Escaped in ' + str(answer) + ' minute(s).')
    else:
        print('Trapped!')
    
    

    
            

    
