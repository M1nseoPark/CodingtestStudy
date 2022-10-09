### 거의 다 맞게 풀었는데 아깝다..
### 큐는 굳이 2개 만들 필요 없었음
### BFS라고 꼭 while q 쓰는 거 아님! 잘 생각해보고 코드 짜기

from collections import deque

n = int(input())
k = int(input())
#### 인덱스는 0부터 시작하는게 구현하기 편함
board = [[0] * n for _ in range(n)]  # 0행 0열부터 시작 (그래프를 모두 0으로 채워줌)
# 사과 위치는 모두 1로 채워줌 -> 이거때매 엄~~청 헤맴
for _ in range(k):
    a, b = map(int, input().split())
    board[a-1][b-1] = 1

l = int(input())
way = {}  #### 딕셔너리로 구현하면 좋음
for _ in range(l):
    a, b = input().split()
    way[int(a)] = b

dx = [1, 0, -1, 0]   # 우, 하, 좌, 상
dy = [0, 1, 0, -1]

snake = deque()
snake.append([0, 0])
board[0][0] = 2  # 뱀이 있는 곳은 2로 채워줌
time = 1

def bfs():
    global time
    ny, nx, d = 0, 0, 0

    while True:
        # 이동하기
        nx = nx + dx[d]
        ny = ny + dy[d]

        if 0 <= nx < n and 0 <= ny < n and board[ny][nx] != 2:
            if board[ny][nx] == 1:   # 사과를 먹고 길이를 늘림
                snake.append([ny, nx])
                board[ny][nx] = 2

            else:  # 빈칸이면 이동만 하고 꼬리 길이를 줄임
                board[ny][nx] = 2
                snake.append([ny, nx])
                ty, tx = snake.popleft()
                board[ty][tx] = 0

            ##### 방향 바꾸기 -> 암기해야 할 코드(5->1 이런 거 생각하느라 시간 꽤 씀)
            if time in way.keys():
                if way[time] == 'D':
                    d = (d + 1) % 4
                else:
                    d = (d - 1) % 4

            time += 1

        else:
            break


bfs()
print(time)
