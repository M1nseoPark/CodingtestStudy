import sys

INF = sys.maxsize

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
bus = [[INF] * (n + 1) for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    bus[a][b] = min(c, bus[a][b])

    
def floyd():
    for i in range(1, n+1):
        for j in range(1, n+1):
            dist[i][j] = bus[i][j]
            route[i][j] = [i, j]

    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    route[i][j] = route[i][k] + route[k][j][1:]
                    

    return dist


dist = [[INF] * (n + 1) for _ in range(n+1)]
route = [[[] for _ in range(n+1)] for _ in range(n+1)]
answer = floyd()

for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j:
            print(0, end=' ')
        elif answer[i][j] == INF:
            print(0, end=' ')
        else:
            print(answer[i][j], end=' ')

    print()

for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j:
            print(0)
        elif answer[i][j] == INF:
            print(0)
        else:
            print(len(route[i][j]), end=' ')
            print(' '.join(map(str, route[i][j])))
            
