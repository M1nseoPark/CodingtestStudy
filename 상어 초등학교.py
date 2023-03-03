n = int(input())
m = n*n
room = [[0] * n for _ in range(n)]
like = [[0] * (m + 1) for _ in range(m+1)]
order = []
for _ in range(m):
    t = list(map(int, input().split()))
    order.append(t[0])
    for i in range(1, 5):
        like[t[0]][t[i]] = 1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def find(num):
    sub = []
    for y in range(n):
        for x in range(n):
            if room[y][x] == 0:
                a, b = 0, 0   # 좋아하는 학생 수, 비어있는 칸 수
                
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0 <= nx < n and 0 <= ny < n:
                        if room[ny][nx] != 0 and like[num][room[ny][nx]] == 1:
                            a += 1
                        elif room[ny][nx] == 0:
                            b += 1

                sub.append([a, b, y, x])

    sub.sort(key=lambda x:(-x[0], -x[1], x[2], x[3]))
    return (sub[0][2], sub[0][3])


score = [[0] * n for _ in range(n)]
for i in range(m):
    y, x = find(order[i])
    room[y][x] = order[i]

for y in range(n):
    for x in range(n):
        s = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and like[room[y][x]][room[ny][nx]] == 1:
                s += 1
        score[y][x] = s

answer = 0
for i in range(n):
    for j in range(n):
        if score[i][j] == 1:
            answer += 1
        elif score[i][j] == 0:
            continue
        else:
            answer += 10 ** (score[i][j] - 1)

print(answer)
    
