import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())
A = deque(map(int, sys.stdin.readline().split()))
robot = deque([0] * n)

stage = 0

while True:
    stage += 1

    # 벨트 한 칸 회전
    A.rotate()
    robot.rotate()
    robot[-1] = 0

    # 로봇 이동
    for i in range(n-1, 0, -1):
        if robot[i] == 0 and robot[i-1] == 1 and A[i] >= 1:
            A[i] -= 1
            robot[i] = 1
            robot[i-1] = 0

    robot[-1] = 0

    # 로봇 올리기 
    if A[0] > 0 and robot[0] == 0:
        robot[0] = 1
        A[0] -= 1

    zero = 0
    # 내구도가 0인 칸의 개수가 k개 이상이면 과정 종료 
    for i in range(2*n):
        if A[i] == 0:
            zero += 1

    if zero >= k:
        break


print(stage)
    
            
