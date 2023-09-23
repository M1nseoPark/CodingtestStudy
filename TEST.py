def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a > b:
        parent[a] = b
    else:
        parent[b] = a

n = int(input())
m = int(input())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

plan = list(map(int, input().split()))
parent = [i for i in range(n)]

edges = set()
for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            temp = [i, j]
            temp.sort()
            edges.add(tuple(temp))

for a, b in edges:
    union_parent(parent, a, b)

answer = 'YES'
for i in range(1, m):
    if parent[plan[0]-1] != parent[plan[i]-1]:
        answer = 'NO'
        break

print(answer)