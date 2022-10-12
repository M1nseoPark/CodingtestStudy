# 맞왜틀
from collections import deque

n, m, t = map(int, input().split())
disk = []
for _ in range(n):
    disk.append(deque(map(int, input().split())))

roll = []
for _ in range(t):
    roll.append(list(map(int, input().split())))

plus = 1000
for w in range(t):
    x, d, k = roll[w][0], roll[w][1], roll[w][2]
    remove = set()

    # 원판을 회전 시킴
    for i in range(x, n+1, x):
        for j in range(k):
            if d == 0:  # 시계 방향
                disk[i-1].appendleft(disk[i-1].pop())
            else:  # 반시계 방향
                disk[i-1].append(disk[i-1].popleft())

    # 인접하면서 수가 같은 거 찾기
    for i in range(n):
        for j in range(m):
            if disk[i][j] != 0:
                left1 = disk[i][(j-1)%m]
                right1 = disk[i][(j+1)%m]

                # print(disk[i][j], left1, right1)
                if disk[i][j] == left1 and disk[i][j] == right1:
                    remove.add((i, j))
                    remove.add((i, (j - 1) % m))
                    remove.add((i, (j + 1) % m))

                elif disk[i][j] == left1:
                    remove.add((i, j))
                    remove.add((i, (j - 1) % m))

                elif disk[i][j] == right1:
                    remove.add((i, j))
                    remove.add((i, (j + 1) % m))

                left2 = disk[(i-1)%n][j]
                right2 = disk[(i+1)%n][j]
                # print(disk[i][j], left2, right2)
                # print('------')
                if i != 0 and i != (n - 1) and disk[i][j] == left2 and disk[i][j] == right2:
                    remove.add((i, j))
                    remove.add(((i - 1) % n, j))
                    remove.add(((i + 1) % n, j))

                elif i != 0 and disk[i][j] == left2:
                    remove.add((i, j))
                    remove.add(((i - 1) % n, j))

                elif i != (n - 1) and disk[i][j] == right2:
                    remove.add((i, j))
                    remove.add(((i + 1) % n, j))

    remove = list(remove)
    # print(remove)
    for i in range(len(remove)):
        disk[remove[i][0]][remove[i][1]] = 0

    plus, num = 0, 0
    for i in range(n):
        for j in range(m):
            plus += disk[i][j]
            if disk[i][j] != 0:
                num += 1

    if len(remove) == 0 and plus != 0 and num != 0:
        # 처음에 이 부분 틀림 -> 정수 나누기가 아닌데 정수 나누기로 풀었음
        rst = plus / num
        for i in range(n):
            for j in range(m):
                if disk[i][j] != 0 and rst > float(disk[i][j]):
                    disk[i][j] += 1
                elif disk[i][j] != 0 and rst < float(disk[i][j]):
                    disk[i][j] -= 1
    elif plus == 0:
        break

print(plus)
