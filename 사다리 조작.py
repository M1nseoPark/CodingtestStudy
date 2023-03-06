# 가로선 연속하면 안됨
# 세로선, 가로선 인덱스 1부터 시작 
# i번 세로선의 결과가 i번이 나오기 위해 추가해야 하는 가로선 개수의 최솟값

n, m, h = map(int, input().split())  # 세로선 개수, 이미 그려진 가로선 개수, 가로선 놓을 수 있는 위치의 개수
graph = [[0] * n for _ in range(h)]

for _ in range(m):
    a, b = map(int, input().split())   # 가로선, 세로선 
    graph[a-1][b-1] = 1

def check():
    for i in range(n):   # 세로선 
        temp = i   # 현재 위치 
        for j in range(h):   # 가로선 
            if graph[j][temp] == 1:   # 1이면 오른쪽 세로선으로 이동
                temp += 1
            elif temp > 0 and graph[j][temp-1] == 1:   # 왼쪽이 1인 경우
                temp -= 1

        if temp != i:
            return False

    return True
                
                
def dfs(cnt, x, y):
    global answer
    if check():   # i번 세로선의 결과가 i번이 나오면 
        answer = min(answer, cnt)
        return
    if cnt == 3 or answer <= cnt:   # cnt가 3이면 다음 호출에서 4가 돼버림, 가로선을 정답보다 많이 만든 경우 확인 필요 X
        return

    for i in range(x, h):  # x~h까지 가로선 
        k = y if i == x else 0   # 가로선이 변경되기 전까진 가로선을 계속해서 탐색, 행이 변경되면 처음부터 탐색
        for j in range(k, n-1):
            if graph[i][j] == 0 and graph[i][j+1] == 0:   # 가로선 연속하면 안되므로
                if j > 0 and graph[i][j-1] == 1:   # 가로선 연속하면 안되므로 
                    continue
                
                graph[i][j] = 1   # 가로선 놓기
                dfs(cnt+1, i, j+2)
                graph[i][j] = 0
                
        
answer = 4   # 정답은 3 이하
dfs(0, 0, 0)
if answer <= 3:
    print(answer)
else:
    print(-1)
    

