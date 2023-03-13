from collections import deque

saw = [[0]]
for _ in range(4):
    saw.append(deque(map(int, input())))
    
k = int(input())
for _ in range(k):
    n, d = map(int, input().split())

    l, r, ld, rd = saw[n][6], saw[n][2], d, d
    move = [[n, d]]
    
    for i in range(n-1, 0, -1):
        if l != saw[i][2]:
            move.append([i, ld*-1])
            l = saw[i][6]
            ld *= -1
        else:
            break

    for i in range(n+1, 5):
        if r != saw[i][6]:
            move.append([i, rd*-1])
            r = saw[i][2]
            rd *= -1
        else:
            break

    for a, b in move:
        if b == 1:   # 시계방향
            m = saw[a].pop()
            saw[a].appendleft(m)
        else:
            m = saw[a].popleft()
            saw[a].append(m)
            

answer = 0
if saw[1][0] == 1:
    answer += 1
if saw[2][0] == 1:
    answer += 2
if saw[3][0] == 1:
    answer += 4
if saw[4][0] == 1:
    answer += 8

print(answer

