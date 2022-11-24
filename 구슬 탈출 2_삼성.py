# 깊이를 함께 큐에 저장해주기

n, m = map(int, input().split())
board = []
for _ in range(n):
    board.append(list(input()))

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
q = []
visited = [[[[0] * m for _ in range(n)] for _ in range(m)] for _ in range(n)]

# 빨간 구슬, 파란 구슬의 위치 찾기
ry, rx, by, bx = [0] * 4
for i in range(n):
    for j in range(m):
        if board[i][j] == 'B':
            by, bx = i, j

        elif board[i][j] == 'R':
            ry, rx = i, j

q.append([ry, rx, by, bx, 1])   # 위치 정보와 depth!!!
visited[ry][rx][by][bx] = True

# 구슬은 한방향으로 이동하기 시작하면 쭉 이동함
def move(y, x, dy, dx):
    count = 0   # 이동한 칸 수

    # 다음 이동이 벽이거나, 현재 위치가 구멍이 아닐 때까지
    while board[y+dy][x+dx] != '#' and board[y][x] != 'O':
        x += dx
        y += dy
        count += 1

    return y, x, count
    

def bfs():
    while q:
        ry, rx, by, bx, depth = q.pop(0)

        # 10번 이하로 움직여서 빼낼 수 없으면 -1 출력
        if depth > 10:
            break

        for i in range(4):
            nry, nrx, rcount = move(ry, rx, dy[i], dx[i])
            nby, nbx, bcount = move(by, bx, dy[i], dx[i])

            # 파란 구슬이 구멍에 빠지면 실패
            if board[nby][nbx] == 'O':
                continue

            # 빨간 구슬이 구멍에 빠지면 성공
            if board[nry][nrx] == 'O':
                print(depth)
                return

            # 빨간 구슬과 파란 구슬은 동시에 같은 칸에 있을 수 없음
            # 코드 내 움직임의 결과는 실제 움직임의 결과와 다름(구슬 각각을 따로 움직인 것)
            # 동시에 움직였다면 이동거리가 많은 구슬이 적은 구슬 앞에 부딪쳐 멈췄을 것
            if nrx == nbx and nry == nby:
                if rcount > bcount:   # 이동 거리가 많은 구슬을 한칸 뒤로
                    nrx -= dx[i]
                    nry -= dy[i]
                else:
                    nbx -= dx[i]
                    nby -= dy[i]

            ## BFS 탐색을 마치고, 방문 여부 확인
            if not visited[nry][nrx][nby][nbx]:
                visited[nry][nrx][nby][nbx] = True
                q.append([nry, nrx, nby, nbx, depth + 1])
            
    print(-1)                
            

bfs()
                
                
                
                
