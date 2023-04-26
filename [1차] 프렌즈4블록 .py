def solution(m, n, board):
    for i in range(m):
        board[i] = list(board[i])

    answer = 0
    rm = set()
    while True:
        # 보드를 순회하며 4블록이 된 곳의 좌표를 집합에 기록
        for i in range(m-1):
            for j in range(n-1):
                t = board[i][j]
                if t == []:
                    continue
                if board[i+1][j] == t and board[i][j+1] == t and board[i+1][j+1] == t:
                    rm.add((i, j)); rm.add((i+1, j))
                    rm.add((i, j+1)); rm.add((i+1, j+1))

        # 지울 부분이 존재한다면 블록을 지움 
        if rm:
            answer += len(rm)
            for i, j in rm:
                board[i][j] = []
            rm = set()
        # 지울 부분이 존재하지 않는다면 종료 
        else:
            return answer

        # 블록을 위에서 아래로 당겨줌 
        while True:
            moved = False
            for i in range(m-1):
                for j in range(n):
                    if board[i][j] and board[i+1][j] == []:
                        board[i+1][j] = board[i][j]
                        board[i][j] = []
                        moved = True

            if not moved:
                break

        
