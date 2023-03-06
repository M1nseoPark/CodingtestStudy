import sys

INF = sys.maxsize

n, m = map(int, sys.stdin.readline().split())
time = [[INF] * n for _ in range(n)]
for _ in range(m):
    a, b, t = map(int, sys.stdin.readline().split())
    time[a-1][b-1] = t

k = int(input())
city = list(map(int, sys.stdin.readline().split()))

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


dist = floyd()
travel = []

# 왕복 거리 구하기
for i in range(len(city)):
    temp = []
    for j in range(n):
        if (city[i] - 1) == j:
            temp.append(0)
        elif dist[city[i]-1][j] == INF or dist[j][city[i]-1] == INF:
            temp.append(INF)
        else:
            temp.append(dist[city[i]-1][j] + dist[j][city[i]-1])

    travel.append(temp)

answer = []
for j in range(n):
    temp = 0
    for i in range(len(city)):
        if temp < travel[i][j]:
            temp = travel[i][j]

    answer.append(temp)

ans = min(answer)
for i in range(n):
    if answer[i] == ans:
        print(i+1, end=' ')
        
        
