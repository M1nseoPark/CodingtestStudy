import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())
belt = deque(map(int, input().split()))
robots = deque([0]*N)

cnt = 0
while True:
    cnt += 1
    # 1. 벨트 회전
    belt.rotate()
    robots.rotate()

    # 내리는 위치에 로봇이 있다면 내린다.
    robots[-1] = 0

    # 2. 벨트위에서 로봇 이동
    if 1 in robots:
        for i in range(N-1, 0, -1): # 끝에서부터 확인
            if not robots[i] and robots[i-1] and belt[i] > 0:
                # 현재 칸 로봇이 없고,
                # 앞 칸의 벨트 위에 로봇이 있고,
                # 현재 칸 내구도가 1이상일 때 옮기기
                belt[i] -= 1  # 내구도 깍고
                robots[i] = 1 # 로봇 O
                robots[i-1] = 0

    # 내리는 위치에 로봇이 있다면 내린다.
    robots[-1] = 0

    # 3. 올리는 위치에 있는 칸의 내구도가 0이 아니라면 올리는 위치에 로봇 올린다.
    if belt[0] > 0 and not robots[0]:
        belt[0] -= 1
        robots[0] = 1
    # 4. 내구도가 0인 칸의 개수가 K개 이상이면 과정 종료
    if belt.count(0) >= K:
        print(cnt)
        break
