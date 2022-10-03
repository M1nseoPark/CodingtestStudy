n, m = map(int, input().split())
r, c, d = map(int, input().split())
place = []
for _ in range(n):
    place.append(list(map(int, input().split())))

cleaned = [[0] * n for _ in range(n)]

# 좌, 하, 우, 상 순서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def vacuum(y, x, w):
    global answer, rotate

    # 네 방향 모두 청소가 이미 되어있거나 벽인 경우에는,
    if rotate == 4:
        # 바라보는 방향을 유지한 채로 한 칸 후진을 하고
        if w == 0 or w == 1:
            ex = x + dx[w+2]
            ey = y + dy[w+2]
        else:
            ex = x + dx[w-2]
            ey = y + dy[w-2]
            
        # 뒤쪽 방향이 벽이 아니면 2번으로 돌아감
        if place[ey][ex] == 0:
            rotate = 0
            vacuum(ey, ex, w)
        else:
            return answer


    nx = x + dx[w]
    ny = y + dy[w]

    # 왼쪽 방향에 아직 청소하지 않은 공간이 존재한다면,
    if 0 <= nx < m and 0 <= ny < n and cleaned[ny][nx] == 0 and place[ny][nx] == 0:
        answer += 1
        rotate = 0
        cleaned[ny][nx] = 1
        # 그 방향으로 회전한 다음 한 칸을 전진하고 1번부터 진행함
        if w == 0:
            vacuum(ny, nx, 3)
        else:
            vacuum(ny, nx, w-1)

    # 왼쪽 방향에 청소할 공간이 없다면,
    else:
        rotate += 1
        # 그 방향으로 회전하고 2번으로 돌아감
        if w == 0:
            vacuum(y, x, 3)
        else:
            vacuum(y, x, w-1)


answer = 1
rotate = 0

cleaned[r][c] = 1
vacuum(r, c, d)
print(answer)

    
