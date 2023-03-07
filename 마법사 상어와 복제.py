from collections import deque
import copy

m, s = map(int, input().split())
fish = {}
for _ in range(m):
    x, y, d = map(int, input().split())
    if (x-1, y-1) in fish:
        fish[(x-1, y-1)].append(d-1)
    else:
        fish[(x-1, y-1)] = [d-1]

sx, sy = map(int, input().split())
sx -= 1; sy -= 1
smell1, smell2 = {}, {}   # 한 번 전 연습, 두 번 전 연습 


fdy = [-1, -1, 0, 1, 1, 1, 0, -1]
fdx = [0, -1, -1, -1, 0, 1, 1, 1]
sdx = [0, -1, 0, 1, 0]
sdy = [0, 0, -1, 0, 1]

def bfs(move):
    global sx, sy
    
    q = deque()
    q.append([sx, sy, 0, '', 0])
    eat = []
    visited = [[0] * 4 for _ in range(4)]
    visited[sx][sy] = 1

    while q:
        x, y, cnt, p, e = q.popleft()

        if cnt == 3:
            eat.append([e, p])
                
        else:
            for i in range(1, 5):
                nx = x + sdx[i]
                ny = y + sdy[i]
                if 0 <= nx < 4 and 0 <= ny < 4 and visited[nx][ny] == 0:
                    visited[nx][ny] == 1
                    if (nx, ny) in move:
                        q.append([nx, ny, cnt+1, p+str(i), e+len(move[(nx, ny)])])
                    else:
                        q.append([nx, ny, cnt+1, p+str(i), e])

    eat.sort(key=lambda x:(-x[0], x[1]))
    print(eat)

    # 물고기 먹기 
    m = eat[0][1]
    print(m)
    for i in range(3):
        sx += sdx[int(m[i])]
        sy += sdy[int(m[i])]

        if (sx, sy) in move:
            smell1[(sx, sy)] = 1
            del move[(sx, sy)]

    
for _ in range(s):
    # 물고기 이동 
    move = {}
    for k, v in fish.items():
        for i in range(len(v)):
            x, y, d = k[0], k[1], v[i]
            
            for j in range(8):
                nx = x + fdx[d]
                ny = y + fdy[d]
                if 0 <= nx < 4 and 0 <= ny < 4 and (nx, ny) != (sx, sy) and (nx, ny) not in smell1 and (nx, ny) not in smell2:
                    if (nx, ny) in move:
                        move[(nx, ny)].append(d)
                    else:
                        move[(nx, ny)] = [d]
                    break

                else:
                    d = (d - 1) % 8

    # 상어 이동
    smell2 = copy.deepcopy(smell1)
    bfs(move)
    print(move)
    print(smell1)
    print(smell2)
    print(sx, sy)


    # 상어 복제
    for k, v in move.items():
        if k in fish:
            fish[k] += v
        else:
            fish[k] = v


answer = 0
for k, v in fish.items():
    answer += len(v)

print(answer)
    

        

    
    
