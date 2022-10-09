student = []
for _ in range(5):
    student.append(list(input()))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

answer = 0
visited = [[0] * 5 for _ in range(5)]


def pick(y, x, da, do):
    global answer
    
    if (do + da) == 7:
        if da >= 4:
            answer += 1

    elif do > 3:
        return
    
    else:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < 5 and 0 <= ny < 5 and visited[ny][nx] == 0:
                visited[ny][nx] = 1
                if student[ny][nx] == 'S':
                    da += 1
                else:
                    do += 1
                
                pick(ny, nx, da, do)
                
                if student[ny][nx] == 'S':
                    da -= 1
                else:
                    do -= 1
                visited[ny][nx] = 0


for i in range(5):
    for j in range(5):
        if student[i][j] == 'S':
            visited[i][j] = 1
            pick(i, j, 1, 0)
            visited[i][j] = 0

        else:
            visited[i][j] = 1
            pick(i, j, 0, 1)
            visited[i][j] = 0
            

print(answer)
        
        
