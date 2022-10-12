# 격자를 돌리는 것이 관건이었던 문제, 이후 구현은 어렵지 않음
from collections import deque

# 입력 받는 부분
n, q = map(int, input().split())
ice = []
for _ in range(2**n):
    ice.append(list(map(int, input().split())))

level = list(map(int, input().split()))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def fire(y, x):
    cnt = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 > nx or 0 > ny or nx >= 2**n or ny >= 2**n:
            continue

        if ice[ny][nx] > 0:
            cnt += 1

    if cnt >= 3:
        return True
    else:
        return False


def rotate(s):
    # 모든 부분 격자를 시계 방향으로 90도 회전시킴 -> 이 부분이 문제의 핵심이었음
    global ice
    new = [[0] * (2**n) for _ in range(2**n)]
    for i in range(0, 2**n, s):
        for j in range(0, 2**n, s):
            for y in range(s):
                for x in range(s):
                    new[i+x][j+s-y-1] = ice[i+y][j+x]

    ice = new
    melt = []
    for i in range(2**n):
        for j in range(2**n):
            if ice[i][j] != 0 and not fire(i, j):
                melt.append([i, j])

    # 얼음을 녹이는 작업과 인접한 칸 동시에 찾으면 틀림 -> 먼저 발견된 얼음을 녹여버리면 이후 결과가 변함
    for i in range(len(melt)):
        y, x = melt[i][0], melt[i][1]
        ice[y][x] -= 1


def bfs(y, x):
    q = deque()
    q.append([y, x])
    rst = 1

    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= nx < 2**n and 0 <= ny < 2**n and visited[ny][nx] == 0 and ice[ny][nx] != 0:
                q.append([ny, nx])
                visited[ny][nx] = 1
                rst += 1

    return rst


for i in range(q):
    rotate(2**level[i])

visited = [[0] * (2**n) for _ in range(2**n)]
answer1, answer2 = 0, 0

for i in range(2**n):
    for j in range(2**n):
        answer1 += ice[i][j]
        if ice[i][j] != 0 and visited[i][j] == 0:
            visited[i][j] = 1
            answer2 = max(bfs(i, j), answer2)

print(answer1)
print(answer2)
