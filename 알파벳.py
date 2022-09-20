# DFS로 풀기 힘든 문제 -> pypy로 풀어야 통과됨

import sys

r, c = map(int, sys.stdin.readline().split())

board = []
for _ in range(r):
    board.append(list(sys.stdin.readline().rstrip()))

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def dfs(x, y):
    global visited, answer

    if answer < len(visited):
        answer = len(visited)
        
    if x < 0 or x >= r or y < 0 or y >= c:
        return False

    # 시간 줄이기 위해 아스키코드 이용!
    if discovered[ord(board[x][y])-65] == 0: 
        visited.append(board[x][y])
        discovered[ord(board[x][y])-65] = 1

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx, ny)

        visited.pop()
        discovered[ord(board[x][y])-65] = 0

        return True

    else:
        return False

discovered = [0] * 65
visited = []
answer = 0
dfs(0, 0)

print(answer)
            
