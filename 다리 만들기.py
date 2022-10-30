# 아예 어떻게 풀어야하는지 감이 안왔던 문제..

import sys
from collections import deque

n = int(input())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 섬을 구분해주는 bfs -> 다른 섬은 다른 숫자로 표시
def island(y, x):
    global count
    q = deque()
    q.append([y, x])
    visited[y][x] = 1
    board[y][x] = count

    while q:
        y, x = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and board[ny][nx] == 1 and visited[ny][nx] == 0:
                visited[ny][nx] = 1
                board[ny][nx] = count
                q.append([ny, nx])

                
# 바다를 건너며 가장 짧은 다리 길이를 구함
# y, x, z로 매개변수를 설정하면 distance 초기화가 애매해짐
def bridge(z):
    global answer
    distance = [[-1] * n for _ in range(n)]
    q = deque()

    for i in range(n):
        for j in range(n):
            if board[i][j] == z:
                q.append([i, j])
                distance[i][j] = 0

    while q:
        y, x = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue

            ### 다른 땅을 만나면 기존 답과 비교하여 짧은 거리 선택
            if board[ny][nx] != 0 and board[ny][nx] != z:
                answer = min(answer, distance[y][x])
                return

            ### 바다를 만나면 거리를 1씩 늘린다
            if board[ny][nx] == 0 and distance[ny][nx] == -1:
                distance[ny][nx] = distance[y][x] + 1
                q.append([ny, nx])
                
visited = [[0] * n for _ in range(n)]
count = 1   # 섬의 종류
answer = n*n

for i in range(n):
    for j in range(n):
        if visited[i][j] == 0 and board[i][j] == 1:
            island(i, j)
            count += 1
            
for i in range(1, count):
    bridge(i)

print(answer)
    

