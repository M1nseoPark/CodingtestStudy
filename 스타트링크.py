from collections import deque
import sys

f, s, g, u, d = map(int, sys.stdin.readline().split())
visited = [0] * (f + 1)

def bfs(v):
    q = deque()
    q.append(v)
    flag = False
    visited[v] = 1  # 이 코드 추가 안해주면 틀림 (올라가거나 내려가므로 v층 방문 체크 필요)

    while q:
        here = q.popleft()

        if here == g:
            print(visited[here] - 1)
            flag = True
            break

        for i in (here + u, here - d):
            if 1 <= i <= f and visited[i] == 0:
                q.append(i)
                visited[i] = visited[here] + 1

    if not flag:
        print('use the stairs')

if s == g:
    print(0)
else:
    bfs(s)
