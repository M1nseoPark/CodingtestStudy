from collections import deque

n, m = map(int, input().split())
light = [[0] * (n + 1) for _ in range(n+1)]
heavy = [[0] * (n + 1) for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    heavy[a][b] = 1
    light[b][a] = 1

def lbfs(v):
    visited = [False for _ in range(n+1)]
    q = deque()
    q.append(v)
    visited[v] = True
    result = 0

    while q:
        here = q.popleft()

        for i in range(1, n+1):
            if not visited[i] and light[here][i] == 1:
                visited[i] = True
                q.append(i)
                result += 1

    return result


def hbfs(v):
    visited = [False for _ in range(n+1)]
    q = deque()
    q.append(v)
    visited[v] = True
    result = 0

    while q:
        here = q.popleft()

        for i in range(1, n+1):
            if not visited[i] and heavy[here][i] == 1:
                visited[i] = True
                q.append(i)
                result += 1

    return result
                


answer = []
for i in range(1, n+1):
    temp1 = lbfs(i)
    temp2 = hbfs(i)
    #print(i, temp1, temp2)
    if temp1 >= (n+1)//2 or temp2 >= (n+1)//2:
        answer.append(i)

print(len(answer))
