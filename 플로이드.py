import sys

INF = sys.maxsize

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
bus = [[INF] * n for _ in range(n)]
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    bus[a-1][b-1] = min(c, bus[a-1][b-1])

    
def floyd():
    dist = [[INF] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            dist[i][j] = bus[i][j]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist


answer = floyd()
for i in range(n):
    for j in range(n):
        if i == j:
            print(0, end=' ')
        elif answer[i][j] == INF:
            print(0, end=' ')
        else:
            print(answer[i][j], end=' ')

    print()
