'''
# 브루트포스로 풀었을 때 자꾸 틀림
# 상대좌표를 잘못 계산한 거 같은데 어디가 틀린건지 못찾음..

n, m = map(int, input().split())
paper = []
for _ in range(n):
    paper.append(list(map(int, input().split())))

dx = [[0, 1, 0, 1],   # ㅁ
      # ㅡ
      [0, 1, 2, 3], [0, 0, 0, 0],
      # ㄴ
      [0, 0, 0, 1], [0, 0, 0, -1], [0, 0, 0, 1], [0, 0, 0, -1],
      [0, 0, 1, 2], [0, 0, -1, -2], [0, 1, 2, 0], [0, -1, -2, 0],
      # ㄹ
      [0, 0, 1, 1], [0, 0, -1, -1], [0, 1, 1, 2], [0, -1, -1, -2],
      # ㅜ
      [0, 1, 2, 1], [0, 1, 2, 1], [0, 0, 0, 1], [0, 0, 0, -1]]

dy = [[0, 0, 1, 1],   # ㅁ
      # ㅡ
      [0, 0, 0, 0], [0, 1, 2, 3],
      # ㄴ
      [0, 1, 2, 2], [0, 1, 2, 2], [0, 1, 2, 0], [0, 1, 2, 0],
      [0, 1, 1, 1], [0, 1, 1, 1], [0, 0, 0, 1], [0, 0, 0, 1],
      # ㄹ
      [0, 1, 1, 2], [0, 1, 1, 2], [0, 0, 1, 1], [0, 0, -1, -1],
      # ㅜ
      [0, 0, 0, 1], [0, 0, 0, -1], [0, 1, 2, 1], [0, 1, 2, 1]]


def put(y, x):
    # (y, x) 자리에 조각 한개씩 놓아봄
    for i in range(19):
        temp = 0
        for j in range(4):
            nx = x + dx[i][j]
            ny = y + dy[i][j]

            if 0 > nx or 0 > ny or m <= nx or n <= ny:
                temp = 0
                break
            else:
                temp += paper[ny][nx]

        if temp != 0:
            answer.append(temp)

            
answer = []    
for y in range(n):
    for x in range(m):
        put(y, x)

print(max(answer))
'''

# 폴리오미노 모양 = DFS 탐색 경로

import sys

n, m = map(int, sys.stdin.readline().split())
papers = []
for _ in range(n):
    papers.append(list(map(int, sys.stdin.readline().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
visited = [[0] * m for _ in range(n)]
maxi = max(map(max, papers))

def dfs(y, x, cnt, rst):
    global answer

    # 탐색을 계속 진행하여도 최댓값에 못미치는 경우 종료
    if rst + maxi * (4 - cnt) <= answer:
        return
    
    if cnt == 4:
        answer = max(answer, rst)
        return

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < m and 0 <= ny < n and visited[ny][nx] == 0:
            # 두번째 블록 연결 후 'ㅏ, ㅓ, ㅗ, ㅜ' 만들기
            if cnt == 2:
                visited[ny][nx] = 1
                # 새로운 좌표에서 탐색하지 않고 기존 좌표로 돌아와 탐색 재개
                dfs(y, x, cnt+1, rst+papers[ny][nx])
                visited[ny][nx] = 0
                
            visited[ny][nx] = 1
            dfs(ny, nx, cnt+1, rst+papers[ny][nx])
            visited[ny][nx] = 0


answer = 0
for i in range(n):
    for j in range(m):
        visited[i][j] = 1
        dfs(i, j, 1, papers[i][j])
        visited[i][j] = 0

print(answer)
