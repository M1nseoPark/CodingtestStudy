n, m = map(int, input().split())
y, x, d = map(int, input().split())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

visited = [[False] * m for _ in range(n)]
visited[y][x] = True

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

while True:
    flag = False

    for i in range(n):
        print(visited[i])
    print('----')

    for i in range(4):
        d = (d - 1) % 4
        y = y + dy[d]
        x = x + dx[d]

        if 0 <= y < n and 0 <= x < m and not visited[y][x]:
            visited[y][x] = True
            flag = True
            break
    
    if not flag:
        if d < 2:
            d += 2
        else:
            d -= 2
        
        y = y + dy[d]
        x = x + dx[d]
        
        if 0 > y or y >= n or 0 > x or x >= m:
            break

answer = 0
for i in range(n):
    for j in range(m):
        if visited[i][j]:
            answer += 1

print(answer)
