# 변수 많이 쓰면 틀릴 확률 높아짐! 최대한 적게 쓰는 방법 고민
# bfs문은 원래 간단하게 짜나??

import sys

n, l, r = map(int, sys.stdin.readline().split())
people = []
for _ in range(n):
    people.append(list(map(int, sys.stdin.readline().split())))

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs(y, x):
    global flag, result
    q = [[y, x]]
    temp = [[y, x]]
    visited[y][x] = 1
    result += people[y][x]

    while q:
        y, x = q.pop(0)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and visited[ny][nx] == 0:
                if l <= abs(people[ny][nx] - people[y][x]) <= r:
                    visited[ny][nx] = 1
                    temp.append([ny, nx])
                    result += people[ny][nx]
                    q.append([ny, nx])
                    flag = True

    return temp


answer = 0
result = 0
while True:
    visited = [[0] * n for _ in range(n)]
    flag = False
    
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0:
                temp = bfs(i, j)

                for k in range(len(temp)):
                    y, x = temp[k]
                    people[y][x] = result // len(temp)

                result = 0

    if flag:
        answer += 1
    else:
        break

print(answer)
        
    
