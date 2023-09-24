## BFS
from collections import deque

n = int(input())
m = int(input())

city = []

for i in range(n):
    city.append(list(map(int, input().split())))
plan = list(map(int, input().split()))

def bfs(s, e):
    q = deque()
    q.append(s)
    visited = [False] * n
    visited[s] = True

    while q:
        here = q.popleft()

        if here == e:
            return True

        for i in range(n):
            if city[here][i] == 1 and not visited[i]:
                visited[i] = True
                q.append(i)

    return False


answer = True
for i in range(m-1):
    if plan[i] != plan[i+1]:
        if not bfs(plan[i]-1, plan[i+1]-1):
            answer = False
            break

if answer:
    print('YES')
else:
    print('NO')


## 유니온 파인드 
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n = int(input())
m = int(input())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

plan = list(map(int, input().split()))
parent = [i for i in range(n)]

for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            union_parent(parent, i, j)

answer = 'YES'
for i in range(1, m):
    if parent[plan[0]-1] != parent[plan[i]-1]:
        answer = 'NO'
        break

print(answer)