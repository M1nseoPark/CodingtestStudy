import sys

INF = sys.maxsize

n, r = map(int, sys.stdin.readline().split())
city = {}
temp = list(sys.stdin.readline().split())
for i in range(n):
    city[temp[i]] = i
    
m = int(sys.stdin.readline())
temp = list(sys.stdin.readline().split())
travel = []
for i in range(m):
    travel.append(city[temp[i]])

k = int(input())
dist = [[INF] * n for _ in range(n)]
tomo = [[INF] * n for _ in range(n)]

for _ in range(k):
    t, ss, es, c = input().split()

    s, e = city[ss], city[es]
    if dist[s][e] > int(c):
        dist[s][e] = int(c)
        dist[e][s] = int(c)

    if t == 'Mugunghwa' or t == 'ITX-Saemaeul' or t == 'ITX-Cheongchun':
        tomo[s][e] = 0
        tomo[e][s] = 0
    elif t == 'S-Train' or t == 'V-Train':
        if tomo[s][e] > int(c) / 2:
            tomo[s][e] = int(c) / 2
            tomo[e][s] = int(c) / 2
    else:
        if tomo[s][e] > int(c):
            tomo[s][e] = int(c)
            tomo[e][s] = int(c)

# 플로이드 
for l in range(n):
    for i in range(n):
        for j in range(n):
            if dist[i][j] > dist[i][l] + dist[l][j]:
                dist[i][j] = dist[i][l] + dist[l][j]
                dist[j][i] = dist[j][l] + dist[l][i]

            if tomo[i][j] > tomo[i][l] + tomo[l][j]:
                tomo[i][j] = tomo[i][l] + tomo[l][j]
                tomo[j][i] = tomo[j][l] + tomo[l][i]

yes, no = r, 0
for i in range(m-1):
    s, e = travel[i], travel[i+1]
    yes += tomo[s][e]
    no += dist[s][e]

if yes >= no:
    print('No')
else:
    print('Yes')
    
    
