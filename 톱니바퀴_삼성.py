wheel = []
for _ in range(4):
    wheel.append(input())

k = int(input())
turn = []
for _ in range(k):
    turn.append(list(map(int, input().split())))


def rotate(n, d):
    left = wheel[n][6]
    right = wheel[n][2]
    lmove = [[n, d]]   # 왼쪽 이동 목록
    rmove = [[n, d]]   # 오른쪽 이동 목록

    # 회전할 목록
    if n != 0:
        for i in range(n-1, -1, -1):
            if wheel[i][2] != wheel[i+1][6]:
                if lmove[-1][1] == -1:
                    lmove.append([i, 1])
                else:
                    lmove.append([i, -1])
            else:
                break

    if n != 3:
        for i in range(n+1, 4):
            if wheel[i-1][2] != wheel[i][6]:
                if rmove[-1][1] == -1:
                    rmove.append([i, 1])
                else:
                    rmove.append([i, -1])
            else:
                break

    # 회전
    for i in range(len(lmove)):
        if lmove[i][1] == -1:
            wheel[lmove[i][0]] += wheel[lmove[i][0]][0]
            wheel[lmove[i][0]] = wheel[lmove[i][0]][1:]
        else:
            wheel[lmove[i][0]] = wheel[lmove[i][0]][-1] + wheel[lmove[i][0]]
            wheel[lmove[i][0]] = wheel[lmove[i][0]][:-1]

    for i in range(1, len(rmove)):
        if rmove[i][1] == -1:
            wheel[rmove[i][0]] += wheel[rmove[i][0]][0]
            wheel[rmove[i][0]] = wheel[rmove[i][0]][1:]
        else:
            wheel[rmove[i][0]] = wheel[rmove[i][0]][-1] + wheel[rmove[i][0]]
            wheel[rmove[i][0]] = wheel[rmove[i][0]][:-1]


for i in range(k):
    rotate(turn[i][0] - 1, turn[i][1])

answer = 0
if wheel[0][0] == '1':
    answer += 1
if wheel[1][0] == '1':
    answer += 2
if wheel[2][0] == '1':
    answer += 4
if wheel[3][0] == '1':
    answer += 8

print(answer)


    

    

    
    
                
                
                
                    
            
            
    
