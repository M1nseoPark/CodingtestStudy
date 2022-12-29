from collections import deque

a, b, c = map(int, input().split())
visited = [[0] * 10000 for _ in range(10000)]

def bfs(a, b, c):
    q = deque()
    q.append([a, b, c])
    visited[a][b] = 1

    while q:
        a, b, c = q.popleft()
        if a == b and b == c:
            return 1

        if a > b and not visited[a-b][2*b]:
            visited[a-b][2*b] = 1
            q.append([a-b, 2*b, c])
        if a < b and not visited[2 * a][b - a]:
            visited[2 * a][b - a] = 1
            q.append([2*a, b-a, c])
        if b > c and not visited[b - c][2 * c]:
            visited[b-c][2*c] = 1
            q.append([a, b-c, 2*c])
        if b < c and not visited[2*b][c-b]:
            visited[2*b][c-b] = 1
            q.append([a, 2*b, c-b])
        if c > a and not visited[2*a][c-a]:
            visited[2*a][c-a] = 1
            q.append([2*a, b, c-a])
        if c < a and not visited[a-c][2*c]:
            visited[a-c][2*c] = 1
            q.append([a-c, b, 2*c])

    return 0


print(bfs(a, b, c))

        
    
