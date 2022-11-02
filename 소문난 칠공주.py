# 십자 모양으로 선택해야 하면 DFS
# 어떤 경우가 이미 선택되었는지 코드를 짜기 힘들었음

seat = []
for _ in range(5):
    seat.append(list(input()))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
visited = [[0] * 5 for _ in range(5)]
result = 0
p = []

def check(num):
    y = num // 5
    x = num % 5

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 > nx or 0 > ny or nx >= 5 or ny >= 5 or visited[ny][nx] == 1:
            continue

        next = ny * 5 + nx  # 다음 숫자
        if next in p:  # p에 있다면 방문 표시, 재귀로 다음 숫자 넘겨 재검사
            visited[ny][nx] = 1
            available += 1
            check(next)
            

# (depth, 임도연파 개수, 사용할 숫자 인덱스)
def dfs(depth, ycnt, idx):
    if ycnt > 3 or 25 - idx < 7 - depth:  # 임도연파가 4명 이상이거나, ..?
        return

    if depth == 7:   # depth가 7에 도달하면 연결 여부 검사
        available = 1
        visited = [[0] * 5 for _ in range(5)]
        sy, sx = p[0]//5, p[0]%5
        visited[sy][sx] = 1
        
        check(p[0])  # 시작 지점을 넘김
        
        if available == 7:
            result += 1
        return

    y = idx // 5
    x = idx % 5

    if seat[y][x] == 'Y':  # 임도연파라면 ycnt+1
        p.append(idx)
        dfs(depth+1, ycnt+1, idx+1)
        p.pop()  # 백트래킹
    else:
        p.append(idx)
        dfs(depth+1, ycnt, idx+1)
        p.pop()
        
    dfs(depth, ycnt, idx+1)  # 사용하지 않고, 그냥 인덱스만 넘김
    
    
        
        
        

        
        
