n, m, k = map(int, input().split())
fire = []
for _ in range(m):
    r, c, m, s, d = map(int, input().split())   # 행, 열, 질량, 속력, 방향 
    fire.append([r-1, c-1, m, s, d])

dc = [0, 1, 1, 1, 0, -1, -1, -1]
dr = [-1, -1, 0, 1, 1, 1, 0, -1]

for _ in range(k):
    board = {}
    for i in range(len(fire)):
        r, c, m, s, d = fire[i]
        nr = (r + dr[d]*s) % n
        nc = (c + dc[d]*s) % n
        
        if (nr, nc) in board:
            board[(nr, nc)].append([m, s, d])
        else:
            board[(nr, nc)] = [[m, s, d]]

    fire = []
    for k, v in board.items():
        if len(v) > 1:
            sm, ss = 0, 0
            sd, flag = v[0][2] % 2, True
            
            for i in range(len(v)):
                sm += v[i][0]
                ss += v[i][1]
                if sd != v[i][2] % 2:
                    flag = False

            m = sm // 5
            s = ss // len(v)
            d = []
            if flag:
                d = [0, 2, 4, 6]
            else:
                d = [1, 3, 5, 7]
                
            if m != 0:
                fire.append([k[0], k[1], m, s, d[0]])
                fire.append([k[0], k[1], m, s, d[1]])
                fire.append([k[0], k[1], m, s, d[2]])
                fire.append([k[0], k[1], m, s, d[3]])

        else:
            fire.append([k[0], k[1], v[0][0], v[0][1], v[0][2]])

answer = 0
for i in range(len(fire)):
    answer += fire[i][2]

print(answer)
    
    
