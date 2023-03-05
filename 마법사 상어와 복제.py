from collections import deque

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
sx1, sy1, sx2, sy2 = -1, -1, -1, -1   # 한 번 전 연습, 두 번 전 연습 


fdy = [-1, -1, 0, 1, 1, 1, 0, -1]
fdx = [0, -1, -1, -1, 0, 1, 1, 1]
sdy = [-1, 1, 0, 0]
sdx = [0, 0, -1, 1]

def bfs(move):
    q = deque()
    q.append([sx, sy, 0, ''])
    eat = []

    while q:
        x, y, cnt, p = q.popleft()

        if cnt == 3:
            if (x, y) in move:
                eat.append([sum(move[(x, y)]), int(p), x, y])
                '''
                if (x, y) in smell2:
                    smell2[(x, y)].append(move[(x, y)])
                else:
                    smell2[(x, y)] = [move[(x, y)]]
                '''
            else:
                eat.append([0, int(p), x, y])
                
        else:
            for i in range(4):
                nx = x + sdx[i]
                ny = y + sdy[i]
                if 0 <= nx < 4 and 0 <= ny < 4:
                    q.append([nx, ny, cnt+1, p+str(i)])

    eat.sort(key=lambda x:(-x[0], x[1]))
    return (eat[0][0], eat[0][2], eat[0][3])

    
for _ in range(s):
    # 물고기 이동 
    move = {}
    for k, v in fish.items():
        for i in range(len(v)):
            x, y, d = k[0], k[1], v[i]
            
            for j in range(8):
                nx = x + fdx[d]
                ny = y + fdy[d]
                if 0 <= nx < 4 and 0 <= ny < 4 and (nx, ny) != (sx, sy) and (nx, ny) != (sx1, sy1) and (nx, ny) != (sx2, sy2):
                    if (nx, ny) in move:
                        move[(nx, ny)].append(d)
                    else:
                        move[(nx, ny)] = [d]
                    break

                else:
                    d = (d - 1) % 8

    # 상어 이동
    e, x, y = bfs(move)
    sx2, sy2 = sx1, sy1
    if e != 0:
        sx1, sy1 = x, y
        del move[(x, y)]

    
    
