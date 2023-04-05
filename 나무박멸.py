# nxn, 나무의 그루 수+벽 정보
# 3) 제초제를 뿌렸을 때 나무가 가장 많이 박멸되는 칸에 뿌림 (행, 열 -> 람다 정렬)
# 3-1) 제초제는 4개의 대각선 방향으로 k칸만큼 전파됨
# 3-2) 벽이나 빈칸 만나면 이 칸까지만 제초제 뿌려지고 이후로는 전파 안됨
# 3-3) 제초제가 뿌려진 칸은 c년만큼 제초제가 남아있다가 c+1년째에 사라짐 
from collections import deque

n, m, k, c = map(int, input().split())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))   # 빈칸 0, 벽 -1, 제초제 -2

tree = {}
for i in range(n):
    for j in range(n):
        if board[i][j] > 0:
            tree[(i, j)] = board[i][j]

dx = [0, 0, -1, 1, -1, 1, -1, 1]
dy = [-1, 1, 0, 0, 1, -1, -1, 1]

# 제초제를 어느 칸에 뿌릴지 결정 
def pick():
    result = []

    for key, val in tree.items():
        y, x = key
        result.append([val, y, x])

        for i in range(4, 8):
            for j in range(1, k+1):
                nx = x + dx[i] * j
                ny = y + dy[i] * j
                if 0 > ny or 0 > nx or ny >= n or nx >= n:
                    break
                
                if board[ny][nx] == 0 or board[ny][nx] == -1:
                    break
                
                result[-1][0] += board[ny][nx]
    
    result.sort(key=lambda x:(-x[0], x[1], x[2]))
    return result[0]


answer = 0
killer = deque()
for year in range(m):
    # 인접한 4개의 칸 중 나무가 있는 칸의 수만큼 나무가 성장함
    for key, val in tree.items():
        y, x = key
        cnt = 0
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < n and 0 <= nx < n and board[ny][nx] > 0:
                cnt += 1
        tree[key] += cnt
        board[y][x] += cnt
    
    # 인접한 4개의 칸 중 빈칸에 번식 (나무 그루 수 // 번식 가능한 칸의 개수)
    breed = []
    for key, val in tree.items():
        y, x = key
        temp = []
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < n and 0 <= nx < n and board[ny][nx] == 0:
                temp.append([ny, nx])

        if len(temp) > 0:
            cnt = val // len(temp)
            for by, bx in temp:
                breed.append([by, bx, cnt])
    
    for by, bx, bz in breed:
        if (by, bx) in tree:
            tree[(by, bx)] += bz
        else:
            tree[(by, bx)] = bz
        board[by][bx] += bz
    
    _, ky, kx = pick()

    # 제초제 뿌림 
    kill = [[ky, kx]]
    answer += board[ky][kx]
    board[ky][kx] = -2
    del tree[(ky, kx)]

    for i in range(4, 8):
        for j in range(1, k+1):
            nx = kx + dx[i] * j
            ny = ky + dy[i] * j
            if 0 > ny or 0 > nx or ny >= n or nx >= n:
                break
                
            if board[ny][nx] == 0 or board[ny][nx] == -1:
                kill.append([ny, nx])
                board[ny][nx] = -2
                break
                
            kill.append([ny, nx])
            answer += board[ny][nx]
            del tree[(ny, nx)]
            board[ny][nx] = -2
    
    killer.append(kill)
    if year > c:
        kill = killer.popleft()
        for ky, kx in kill:
            board[ky][kx] = 0

print(answer)
