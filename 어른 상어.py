n, m, k = map(int, input().split())
smell = {}
shark = {}
for i in range(n):
    temp = list(map(int, input().split()))
    for j in range(n):
        if temp[j] != 0:
            smell[(i, j)] = [temp[j], k]
            shark[temp[j]] = [i, j]

temp = [0] + list(map(int, input().split()))
for i in range(1, m+1):
    shark[i].append(temp[i])
    
prior = [[] for _ in range(m+1)]
dx = [0, 0, 0, -1, 1]
dy = [0, -1, 1, 0, 0]

for i in range(1, m+1):
    for j in range(4):   # 위,아래,왼쪽,오른쪽 
        prior[i].append(list(map(int, input().split())))

time = 0
answer = 0

while True:
    if time > 1000:
        answer = -1
        break

    if len(shark) == 1:
        answer = time
        break

    move = {}
    
    # 상어 이동 위치 결정 
    for key, val in shark.items():
        y, x, d = val[0], val[1], val[2]
        flag = False

        for j in range(4):
            ny = y + dy[prior[key][d-1][j]]
            nx = x + dx[prior[key][d-1][j]]
            nd = prior[key][d-1][j]

            if 0 <= ny < n and 0 <= nx < n and (ny, nx) not in smell:
                flag = True
                break

        if not flag:
            for j in range(4):
                ny = y + dy[prior[key][d-1][j]]
                nx = x + dx[prior[key][d-1][j]]
                nd = prior[key][d-1][j]

                if 0 <= ny < n and 0 <= nx < n and smell[(ny, nx)][0] == key:
                    break

        move[key] = [ny, nx, nd]

    move = sorted(move.items())

    # 상어 이동 + 쫒아냄 
    check = {}
    for i in range(len(move)):
        key, y, x, d = move[i][0], move[i][1][0], move[i][1][1], move[i][1][2]
        shark[key] = [y, x, d]
        if (y, x) in check:
            del shark[key]
        else:
            check[(y, x)] = 1

    # 냄새 사라짐 
    dele = []
    for key, val in smell.items():
        smell[key][1] -= 1
        if smell[key][1] == 0:
            dele.append(key)

    for i in dele:
        del smell[i]

    # 냄새 뿌림
    for key, val in shark.items():
        y, x, d = val[0], val[1], val[2]
        smell[(y, x)] = [key, k]
    
    time += 1


print(answer)
