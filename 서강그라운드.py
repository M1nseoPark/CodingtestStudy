import sys

INF = sys.maxsize

n, m, r = map(int, sys.stdin.readline().split())
item = list(map(int, sys.stdin.readline().split()))
maps = [[INF] * n for _ in range(n)]
for _ in range(r):
    a, b, l = map(int, sys.stdin.readline().split())
    maps[a-1][b-1] = l
    maps[b-1][a-1] = l


def floyd():
    dist = [[INF] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if maps[i][j] <= m:
                dist[i][j] = maps[i][j]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    if dist[i][k] + dist[k][j] <= m:
                        dist[i][j] = dist[i][k] + dist[k][j]

    return dist


result = floyd()
answer = [0] * n
for i in range(n):
    answer[i] += item[i]
    
for i in range(n):
    for j in range(n):
        if i != j and result[i][j] != INF:
            answer[i] += item[j]

print(max(answer))
            
        
