seat = []
for _ in range(5):
    seat.append(list(input()))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def pick(sy, sx, s):
    global answer
    visited = [[0] * 5 for _ in range(5)]
    
    while q:
        y, x = q.pop(0)
        print(s)

        if len(s) == 7:
            idx = 0
            for i in s:
                if i == 'S':
                    idx += 1
            if idx >= 4:
                answer += 1
                return
            
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if sx <= nx < 5 and sy <= ny < 5 and visited[ny][nx] == 0:
                q.append([ny, nx])
                s.append(seat[ny][nx])
                visited[ny][nx] = 1
                

q = []
s = []
answer = 0
for i in range(5):
    for j in range(5):
        q.append([i, j])
        s.append(seat[i][j])
        pick(i, j, s)
        q.clear()
        s.clear()

print(answer)
        
        
