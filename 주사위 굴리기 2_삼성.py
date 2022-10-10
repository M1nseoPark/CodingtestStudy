from collections import deque

n, m, k = map(int, input().split())
maps = []
for _ in range(n):
    maps.append(list(map(int, input().split())))

dice = [1, 2, 3, 4, 5, 6]
dy = [0, 1, 0, -1]  # 동남서북 
dx = [1, 0, -1, 0]

def roll(dir):
    a, b, c, d, e, f = dice[0], dice[1], dice[2], dice[3], dice[4], dice[5]
    if dir == 0:  # 동
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = d, b, a, f, e, c
    elif dir == 1:  # 남
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = b, f, c, d, a, e
    elif dir == 2:  # 서
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = c, b, f, a, e, d
    else:  # 북
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = e, a, c, d, f, b


# BFS로 풀면 되는데 왜 생각 못했지?
def score(y, x, s):
    count = 0
    q = deque()
    q.append([y, x])
    visited = [[0] * m for _ in range(n)]
    visited[y][x] = 1
    
    while q:
        y, x = q.popleft()
        count += 1
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= nx < m and 0 <= ny < n and visited[ny][nx] == 0 and maps[ny][nx] == s:
                q.append([ny, nx])
                visited[ny][nx] = 1

    return count * s


answer = 0
way = 0
x, y = 0, 0
for _ in range(k):
    # 이동 방향으로 한 칸 굴러감
    if 0 <= y + dy[way] < n and 0 <= x + dx[way] < m:
        y += dy[way]
        x += dx[way]
        answer += score(y, x, maps[y][x])
        roll(way)

        if dice[-1] > maps[y][x]:
            way = (way + 1) % 4
        elif dice[-1] < maps[y][x]:
            way = (way - 1) % 4

    # 이동 방향에 칸이 없다면, 이동 방향을 반대로 한 다음 한 칸 굴러감
    else:
        if way == 0 or way == 1:
            way += 2
        else:
            way -= 2

        y += dy[way]
        x += dx[way]
        answer += score(y, x, maps[y][x])
        roll(way)

        if dice[-1] > maps[y][x]:
            way = (way + 1) % 4
        elif dice[-1] < maps[y][x]:
            way = (way - 1) % 4

print(answer)
