def solution(n, build_frame):
    answer = []
    board = [[[0] * 2 for _ in range(n+1)] for _ in range(n+1)]  # 기둥, 보
    
    def check(y, x, type):
        if type == 0:  # 기둥
            if (y == 0) or (x-1 >= 0 and board[y][x-1][1] == 1) or board[y-1][x][0] == 1:
                return True
        else:  # 보 
            if (y > 0 and board[y-1][x][0] == 1) or (y > 0 and x < n and board[y-1][x+1][0] == 1) or ((x-1 >= 0 and board[y][x-1][1] == 1) and (x < n and board[y][x+1][1] == 1)):
                return True
            
        return False
    
    
    for x, y, a, b in build_frame:
        if b == 1:  # 설치
            if check(y, x, a):
                board[y][x][a] = 1
                    
        else:  # 삭제
            if a == 0:  # 기둥 
                board[y][x][0] = 0
                if not ((board[y][x][1] == 0 or check(y, x, 1)) and (y+1 > n or board[y+1][x][0] == 0 or check(y+1, x, 0)) and (x-1 < 0 or board[y][x-1][1] == 0 or check(y, x-1, 1))):
                    board[y][x][0] = 1

            else:  # 보
                board[y][x][1] = 0
                if not ((board[y][x][0] == 0 or check(y, x, 0)) and (x+1 > n or board[y][x+1][1] == 0 or check(y, x+1, 1)) and (x-1 < 0 or board[y][x-1][1] == 0 or check(y, x-1, 1)) and (x+1 > n or board[y][x+1][0] == 0 or check(y, x+1, 0))):
                    board[y][x][1] = 1
    
    for y in range(n+1):
        for x in range(n+1):
            if board[y][x][0] == 1:
                answer.append([x, y, 0])
            if board[y][x][1] == 1:
                answer.append([x, y, 1])
    
    answer.sort()
    return answer

solution(5, [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]])