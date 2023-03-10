n = int(input())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

wind = [{(-2, 0):0.02, (-1, -1):0.10, (-1, 0):0.07, (-1, 1):0.01,
         (0, -2):0.05, (0, -1):0.55, (1, -1):0.10, (1, 0):0.07, (1, 1):0.01,
         (2, 0):0.02},   # 서
        {(0, -2):0.02, (1, -1):0.10, (0, -1):0.07, (-1, -1):0.01,
         (-2, 0):0.05, (1, 0):0.55, (1, 1):0.10, (0, 1):0.07, (-1, 1):0.01,
         (0, 2):0.02},   # 남 
        {(2, 0):0.02, (1, 1):0.10, (1, 0):0.07, (1, -1):0.01,
         (0, 2):0.05, (0, 1):0.55, (-1, 1):0.10, (-1, 0):0.07, (-1, -1):0.01,
         (-2, 0):0.02},   # 동 
        {(0, 2):0.02, (-1, 1):0.10, (0, 1):0.07, (1, 1):0.01,
         (-2, 0):0.05, (-1, 0):0.55, (-1, -1):0.10, (0, -1):0.07, (1, -1):0.01,
         (0, -2):0.02}]   # 북

y, x, i = n//2, n//2, 0
answer = 0

dy = [0, 1, 0, -1]
dx = [-1, 0, 1, 0]
way = []

a, b = 1, 0
while True:
    if len(way) >= n*n:
        break
    
    for _ in range(2):
        for j in range(a):
            way.append(b)
        b += 1
    a += 1

        
while True:
    if y == 0 and x == 0:
        break

    d = way[i] % 4
    y += dy[d]
    x += dx[d]
    
    sand = board[y][x]
    board[y][x] = 0

    for k, v in wind[d].items():
        ny = y + k[0]
        nx = x + k[1]
        if 0 <= ny < n and 0 <= nx < n:
            board[ny][nx] += int(sand * v)
        else:
            answer += int(sand * v)

    for i in range(n):
        print(board[i])
    print('------')

    i += 1


print(answer)

    

    
    

