from collections import deque

maps = []
for _ in range(12):
    maps.append(list(input()))

score = 0

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def burst(color):
    global result
    visited = [[0] * 6 for _ in range(12)]

    while True:
        q = deque()
        link = []
        find = False

        for i in range(12):
            for j in range(6):
                if maps[i][j] == color and visited[i][j] == 0:
                    q.append([i, j])
                    link.append([i, j])
                    visited[i][j] = 1
                    find = True
                    break

            if len(q) != 0:
                break

        if not find:
            break

        while q:
            y, x = q.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < 6 and 0 <= ny < 12 and visited[ny][nx] == 0 and maps[ny][nx] == color:
                    q.append([ny, nx])
                    visited[ny][nx] = 1
                    link.append([ny, nx])

        if len(link) >= 4:
            result += link
    

while True:
    result = []
    
    burst('R')
    burst('G')
    burst('B')
    burst('P')
    burst('Y')

    if len(result) != 0:
        score += 1
    else:
        break

    for i in range(len(result)):
        y, x = result[i][0], result[i][1]
        maps[y][x] = '.'

    # 뿌요 아래로 떨어짐 
    for i in range(6):
        end = 0
        for j in range(11, -1, -1):
            if end == 0 and maps[j][i] == '.':
                end = j

            if end != 0 and maps[j][i] != '.':
                maps[j][i], maps[end][i] = maps[end][i], maps[j][i]
                end -= 1


print(score)
    
                
            
