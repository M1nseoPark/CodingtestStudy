# (4x4) 크기
# 한 칸에 물고기 한 마리 존재 -> 번호와 방향 가짐(1~16, 상하좌우대각선 방향)
# 첨에 (0,0) 물고기 먹고, (0,0) 물고기의 방향 가지게 됨

# 번호가 작은 '물고기'부터 순서대로 이동함 -> 상어가 있는 칸 이동 불가
## 이동할 수 있을 때까지 반시계 45도 회전, 이동할 수 있는 칸이 없으면 이동하지 않음
## 서로의 위치를 바꾸는 방법으로 이동함

# 상어는 방향에 따라 여러 칸 이동 가능, 이동한 칸 물고기 먹으면 먹은 물고기의 방향 가짐
## '도착한 칸'의 물고기를 먹음
## 물고기가 없는 칸으로는 이동할 수 없음 -> 집에 감 

dy = [-1, -1, 0, 1, 1, 1, 0, -1]
dx = [0, -1, -1, -1, 0, 1, 1, 1]

sea = [[0] * 4 for _ in range(4)]
dic = {}
for i in range(4):
    temp = list(map(int, input().split()))
    for j in range(0, 7, 2):
        sea[i][j//2] = temp[j]
        dic[temp[j]] = [i, j//2, temp[j+1]-1]


# 물고기 이동 
def move(sy, sx):
    for i in range(1, 17):
        if i in dic:
            y, x, d = dic[i]
            flag = False

            ny = y + dy[d]
            nx = x + dx[d]

            if 0 <= ny < 4 and 0 <= nx < 4 and (ny != sy or nx != sx):
                flag = True
            else:
                for _ in range(8):
                    d = (d + 1) % 8
                    ny = y + dy[d]
                    nx = x + dx[d]
                    if 0 <= ny < 4 and 0 <= nx < 4 and (ny != sy or nx != sx):
                        flag = True
                        break

            if flag:
                if sea[ny][nx] == 0:
                    sea[ny][nx], sea[y][x] = sea[y][x], sea[ny][nx]
                    dic[i] = [ny, nx, d]
                else:
                    idx = sea[ny][nx]
                    sea[ny][nx], sea[y][x] = sea[y][x], sea[ny][nx]
                    dic[i] = [ny, nx, d]
                    dic[idx][0], dic[idx][1] = y, x
            
    
def dfs(sy, sx, sd, ans):
    global answer
    
    move(sy, sx)
    end = True

    while 0 <= (sy + dy[sd]) < 4 and 0 <= (sx + dx[sd]) < 4:
        sy += dy[sd]
        sx += dx[sd]

        if sea[sy][sx] != 0:
            end = False
            idx = sea[sy][sx]
            fy, fx, fd = dic[idx]
            del dic[idx]
            sea[sy][sx] = 0

            dfs(sy, sx, fd, ans+idx)

            dic[idx] = [fy, fx, fd]
            sea[sy][sx] = idx

    if end:
        answer = max(answer, ans)
        return
        

idx = sea[0][0]
sy, sx, sd = 0, 0, dic[idx][2]
sea[0][0] = 0
del dic[idx]
        
answer = 0
dfs(sy, sx, sd, idx)
print(answer)
