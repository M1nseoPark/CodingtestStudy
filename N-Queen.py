# 상하좌우, 대각선 같은 줄에 이미 퀸이 있을 경우,
# 다음 퀸 놓지 않아도 됨(백트래킹)
# 현재 놓는 퀸이 n번째 퀸일 경우 방법의 수 1 증가

n = int(input())
row = [0] * n   # 굳이 이차원 리스트를 만들 필요 없음!

def adjacent(x):
    for i in range(x):
        # 열이 같거나 대각선이 같으면 False
        if row[x] == row[i] or abs(row[x] - row[i]) == x - i:
            return False

    return True


def dfs(x):
    global answer

    if x == n:
        answer += 1
    else:
        # 각 행에 퀸 놓기
        for i in range(n):   # i는 0~(n-1)열에서 유망한 곳 찾기
            row[x] = i
            if adjacent(x):  # 행,열,대각선 체크함수 -> True이면 계속 진행
                dfs(x + 1)  

answer = 0
dfs(0)
print(answer)
