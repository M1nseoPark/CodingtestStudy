# 2번 선수의 순위를 알기 위해서는
# 1) 2번에서 1,3,4,5번 선수까지 가는 경로가 존재하거나
# 2) 각 선수에서 2번까지 가는 경로가 존재한다면, 2번 선수의 순위를 매길 수 있음
def solution(n, results):
    answer = 0
    board = [[0] * n for _ in range(n)]

    for a, b in results:
        board[a-1][b-1] = 1
        board[b-1][a-1] = -1
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if i == j or board[i][j] in [1, -1]:
                    continue

                if board[i][k] == board[k][j] == 1:
                    board[i][j] = 1
                    board[j][i] = board[k][i] = board[j][k] = -1
    
    for row in board:
        # 자기자신만 0 -> 자기자신 제외 모든 나머지 선수들과 경기 결과가 있음 
        if row.count(0) == 1:
            answer += 1
    
    return answer 
