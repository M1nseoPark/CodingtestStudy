# 현재 위치에서 바로 다음에 갈 수 있는 인덱스 
graph = [[1],[2],[3],[4],[5],[6, 21],[7],[8],[9],[10],[11, 25],[12],[13],[14],
         [15],[16, 27],[17],[18],[19],[20],[32],[22],[23],[24],[30],[26],[24],
         [28],[29],[24],[31],[20],[32]]
score = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34,
         36, 38, 40, 13, 16, 19, 25, 22, 24, 28, 27, 26, 30, 35, 0]

dice = list(map(int, input().split()))
answer = 0

def count(idx, rst, marker):
    global answer
    if idx >= 10:
        answer = max(answer, rst)
        return

    for i in range(4):   # 말 4개
        x = marker[i]   # 현재 i번째 말의 위치 
        if len(graph[x]) == 2:   # 다음에 갈 수 있는 위치가 두 곳 이면 (초기 1번 이동) 
            x = graph[x][1]   # 파란색 화살표로 이동(-> 파란색 화살표 타야한다고 조건에 나옴)
        else:
            x = graph[x][0]

        for j in range(1, dice[idx]):   # (주사위 수-1)만큼 말 이동
            x = graph[x][0]

        if x == 32 or (x < 32 and x not in marker):
            before = marker[i]   # 현재 i번째 말의 위치 
            marker[i] = x   # 이동 완료한 i번째 말의 위치
            count(idx+1, rst+score[x], marker)
            marker[i] = before


count(0, 0, [0, 0, 0, 0])
print(answer)
        

    

