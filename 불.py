# 디큐 안쓰면 시간초과..

import sys
from collections import deque

test = int(sys.stdin.readline())

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def fbfs():
    while fq:
        y, x = fq.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < w and 0 <= ny < h and maps[ny][nx] != '#' and fvisited[ny][nx] == 0:
                fvisited[ny][nx] = fvisited[y][x] + 1
                fq.append([ny, nx])


def sbfs(y, x):
    q = deque()
    q.append([y, x])
    svisited[y][x] = 1
    result = 0

    while q:
        y, x = q.popleft()

        if y == 0 or y == (h - 1) or x == 0 or x == (w - 1):
            result = svisited[y][x]
            break

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < w and 0 <= ny < h and maps[ny][nx] != '#':
                if svisited[ny][nx] == 0 and (fvisited[ny][nx] == 0 or fvisited[ny][nx] > (svisited[y][x] + 1)):
                    svisited[ny][nx] = svisited[y][x] + 1
                    q.append([ny, nx])

    return result
                
    

for _ in range(test):
    w, h = map(int, sys.stdin.readline().split())
    maps = []
    fq = deque()
    answer = 0

    fvisited = [[0] * w for _ in range(h)]
    svisited = [[0] * w for _ in range(h)]
    
    for i in range(h):
        maps.append(list(sys.stdin.readline().rstrip()))

    for i in range(h):
        for j in range(w):
            if maps[i][j] == '*':
                fq.append([i, j])
                fvisited[i][j] = 1

    fbfs()

    for i in range(h):
        for j in range(w):
            if maps[i][j] == '@':
                answer = sbfs(i, j)
                break


    if answer != 0:
        print(answer)
    else:
        print('IMPOSSIBLE')
    

    

    
