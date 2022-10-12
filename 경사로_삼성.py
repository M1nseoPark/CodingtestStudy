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
        if line[i] < line[i-1]:
            for j in range(l):
                if i + j >= n or line[i] != line[i+j] or visited[i+j]:
                    return False
                if line[i] == line[i+j]:
                    visited[i+j] = True
                    
        elif line[i] > line[i-1]:
            for j in range(l):
                if i - j - 1 < 0 or line[i-1] != line[i-j-1] or visited[i-j-1]:
                    return False
                if line[i-1] == line[i-j-1]:
                    visited[i-j-1] = True

    return True



# 가로줄 확인
for i in range(n):
    visited = [False for _ in range(n)]
    if check([maps[i][j] for j in range(n)]):
        answer += 1

# 세로줄 확인
for j in range(n):
    visited = [False for _ in range(n)]
    if check([maps[i][j] for i in range(n)]):
        answer += 1

print(answer)
             

