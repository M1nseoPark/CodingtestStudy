from collections import deque

r, c = map(int, input().split())
maze = []
for _ in range(r):
    maze.append(list(input()))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
fvisited = [[0] * c for _ in range(r)]

fq = deque()
jq = deque()
for i in range(r):
    for j in range(c):
        if maze[i][j] == 'J':
            jq.append([i, j])

        if maze[i][j] == 'F':
            fq.append([i, j])
            fvisited[i][j] = 1
            

def fbfs():
    while fq:
        y, x = fq.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < c and 0 <= ny < r:
                if maze[ny][nx] != '#' and fvisited[ny][nx] == 0:
                    fvisited[ny][nx] = fvisited[y][x] + 1
                    fq.append([ny, nx])

jvisited = [[0] * c for _ in range(r)]
jvisited[jq[0][0]][jq[0][1]] = 1


def jbfs():
    answer = 0
    
    while jq:
        y, x = jq.popleft()

        if y == 0 or x == 0 or y == (r - 1) or x == (c - 1):
            answer = jvisited[y][x]
            break

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < c and 0 <= ny < r:
                if maze[ny][nx] != '#' and jvisited[ny][nx] == 0:
                    if fvisited[ny][nx] > jvisited[ny][nx]:
                        jvisited[ny][nx] = jvisited[y][x] + 1
                        jq.append([ny, nx])

    if answer == -1:
        print('IMPOSSIBLE')
    else:
        print(answer)

fbfs()
jbfs()

        
                

            
    
    




    
    
