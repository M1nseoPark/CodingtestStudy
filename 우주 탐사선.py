import sys

INF = sys.maxsize

n, k = map(int, input().split())
time = []
for _ in range(n):
    time.append(list(map(int, input().split())))

def floyd():
    dist = [[INF] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            dist[i][j] = time[i][j]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist


def pick(s, visited, d, t):
    if d == n:
        answer.append(t)
        return

    for i in range(n):
        if not visited[i]:
            visited[i] = True
            pick(i, visited, d+1, t+dist[s][i])
            visited[i] = False
        
    
dist = floyd()

visited = [False for _ in range(n)]
visited[k] = True

answer = []
pick(k, visited, 1, 0)
print(min(answer))

    
