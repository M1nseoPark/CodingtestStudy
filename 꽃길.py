n = int(input())
land = []
for _ in range(n):
    land.append(list(map(int, input().split())))

visited = [[False] * n for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def flower(y, x):
    flag = True
    temp = 0
    
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 > ny or 0 > nx or ny >= n or nx >= n:
            flag = False
            break

        if visited[ny][nx]:
            flag = False
            break

    if flag:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            temp += land[ny][nx]
            visited[ny][nx] = True
        return temp
    else:
        return False

    
def plant(d, cnt):
    global answer
    
    if d == 3:
        answer = min(answer, cnt)
        return

    else:
        for i in range(n):
            for j in range(n):
                if not visited[i][j]:
                    temp = flower(i, j)
                    if temp:
                        visited[i][j] = True
                        plant(d+1, cnt+land[i][j]+temp)
                        visited[i][j] = False
                        for k in range(4):
                            visited[i+dy[k]][j+dx[k]] = False
                

answer = 200000000
plant(0, 0)
print(answer)
