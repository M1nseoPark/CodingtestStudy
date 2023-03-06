from collections import deque
import sys

n, k = map(int, sys.stdin.readline().split())
A = deque(map(int, sys.stdin.readline().split()))

stage = 1
robot = [0] * n

while True:
    # 벨트 한칸 회전 
    A.rotate()
    robot = [0] + robot[:-1]

    # 로봇 이동 
    if robot[-1] == 1:
        robot[-1] = 0
    for i in range(n-2, -1, -1):
        if robot[i] == 1 and robot[i+1] == 0 and A[i+1] > 0:
            robot[i], robot[i+1] = robot[i+1], robot[i]
            A[i+1] -= 1

    # 로봇 올림
    if A[0] != 0:
        robot[0] = 1
        A[0] -= 1

    # 종료 조건에 도달했는지 검사
    zero = 0
    for i in range(2*n):
        if A[i] == 0:
            zero += 1

    if zero >= k:
        break

    stage += 1

print(stage)
            
