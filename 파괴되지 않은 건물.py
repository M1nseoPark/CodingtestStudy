def solution(board, skill):
    answer = 0
    n, m = len(board), len(board[0])
    note = [[0] * (m+1) for _ in range(n+1)]   # 누적합 기록을 위한 배열 

    for type, r1, c1, r2, c2, degree in skill:
        if type == 2:
            note[r1][c1] += degree
            note[r1][c2+1] += -degree
            note[r2+1][c1] += -degree
            note[r2+1][c2+1] += degree
        else:
            note[r1][c1] += -degree
            note[r1][c2+1] += degree
            note[r2+1][c1] += degree
            note[r2+1][c2+1] += -degree
    
    # 행 기준 누적합 
    for i in range(n):
        for j in range(m):
            note[i][j+1] += note[i][j]
    
    # 열 기준 누적합 
    for j in range(m):
        for i in range(n):
            note[i+1][j] += note[i][j]
    
    # 기존 리스트와 합함 
    for i in range(n):
        for j in range(m):
            board[i][j] += note[i][j]
            if board[i][j] > 0:
                answer += 1
    
    return answer