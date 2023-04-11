# 내가 이문제를 못푼건.. 걍 구현력이 딸려서야..

# 입력 부분
n, l = map(int, input().split())
maps = []
for _ in range(n):
    maps.append(list(map(int, input().split())))

answer = 0


# 가로와 세로줄만 받아서 확인하는 함수
# 나는 가로줄 확인하는 2중 for문, 세로줄 확인하는 2중 for문 따로 만들었는데 비효율적이었음
# 이렇게 줄로 받으면 됨! -> 아이디어
def check(line):
    for i in range(1, n):
        # 높이 차이가 2 이상인 경우에는 방향 상관없이 무조건 False
        if abs(line[i] - line[i-1]) > 1:
            return False

        # 앞쪽이 더 클때, 뒤쪽이 더 클때 따로 처리해줘야 함!
        # 내리막길(2 1(i) 1 1)
        if line[i] < line[i-1]:
            for j in range(l):
                # 경사로를 놓다가 범위를 벗어나는 경우 or 낮은 지점의 칸의 높이가 같지 않거나 or 놓은 곳에 또 놓는 경우 
                if i + j >= n or line[i] != line[i+j] or visited[i+j]:
                    return False
                if line[i] == line[i+j]:
                    visited[i+j] = True

        # 오르막길(1 1 1(i-1) 2)
        elif line[i] > line[i-1]:
            for j in range(l):
                if i - 1 - j < 0 or line[i-1] != line[i-1-j] or visited[i-1-j]:
                    return False
                if line[i-1] == line[i-1-j]:
                    visited[i-1-j] = True

    return True



# 가로줄 확인
for i in range(n):
    # 경사로를 놓은 위치 표시 
    visited = [False for _ in range(n)]
    if check([maps[i][j] for j in range(n)]):
        answer += 1

# 세로줄 확인
for j in range(n):
    visited = [False for _ in range(n)]
    if check([maps[i][j] for i in range(n)]):
        answer += 1

print(answer)
             

