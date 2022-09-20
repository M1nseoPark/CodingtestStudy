n = int(input())
picture = []
for _ in range(n):
    picture.append(list(input()))

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def dfs(x, y):
    if x < 0 or x >= n or y < 0 or y >= n:
        return False

    if picture[x][y] == 'R':
        picture[x][y] = 'C'

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            rdfs(nx, ny)

        return True
    
    else:
        return False


def gdfs(x, y):
    if x < 0 or x >= n or y < 0 or y >= n:
        return False

    if picture[x][y] == 'G':
        picture[x][y] = 'C'

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            gdfs(nx, ny)

        return True
    
    else:
        return False


def bdfs(x, y):
    if x < 0 or x >= n or y < 0 or y >= n:
        return False

    if picture[x][y] == 'B':
        picture[x][y] = 'X'

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            bdfs(nx, ny)

        return True
    
    else:
        return False


def cdfs(x, y):
    if x < 0 or x >= n or y < 0 or y >= n:
        return False

    if picture[x][y] == 'C':
        picture[x][y] = 'X'

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            cdfs(nx, ny)

        return True
    
    else:
        return False

area = [0] * 4
for i in range(n):
    for j in range(n):
        if rdfs(i, j):
            area[0] += 1
        if gdfs(i, j):
            area[1] += 1
        if bdfs(i, j):
            area[2] += 1
        if cdfs(i, j):
            area[3] += 1

for i in range(n):
    print(picture[i])
print(area)
        

        

