from collections import deque

n, l, r = map(int, input().split())
A = []
for _ in range(n):
    A.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
day = 0

while True:
    visited = [[0] * n for _ in range(n)]
    flag = False

    def bfs(y, x):
        q = deque()
        q.append([y, x])
        visited[y][x] = 1
        dic = {}
        dic[(y, x)] = A[y][x]
        temp = False

        while q:
            y, x = q.popleft()
            
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                if 0 <= nx < n and 0 <= ny < n and visited[ny][nx] == 0:
                    if l <= abs(A[y][x] - A[ny][nx]) <= r:
                        visited[ny][nx] = 1
                        q.append([ny, nx])
                        dic[(ny, nx)] = A[ny][nx]
                        temp = True

        rst = sum(dic.values()) // len(dic)
        for k, v in dic.items():
            A[k[0]][k[1]] = rst

        return temp
    
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0:
                if bfs(i, j):
                    flag = True

    if not flag:
        break

    day += 1

print(day)
    
