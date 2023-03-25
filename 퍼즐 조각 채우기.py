import copy

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def solution(game_board, table):
    global n
    n = len(game_board)
    answer = 0
    blank = []

    # game_board의 빈칸 좌표를 구해서 0,0좌표를 기준으로 옮기기 
    for i in range(n):
        for j in range(n):
            if game_board[i][j] == 0:
                blank.append(dfs(game_board, i, j, [0, 0], 0))

    for k in range(4):
        table = rotate(table)
        temp = copy.deepcopy(table)

        for i in range(n):
            for j in range(n):
                if temp[i][j] == 1:
                    block = dfs(temp, i, j, [0, 0], 1)
                    if block in blank:
                        blank.remove(block)
                        answer += len(block)
                        table = copy.deepcopy(temp)   # dfs내 방문처리 때문 
                    else:
                        temp = copy.deepcopy(table)

    return answer


def dfs(board, y, x, pos, d):
    global n
    result = [pos]
    
    board[y][x] = 2   # 방문 처리

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < n and board[ny][nx] == d:
            result += dfs(board, ny, nx, [pos[0]+dy[i], pos[1]+dy[i]], d)

    return result


def rotate(table):
    n = len(table)
    rotated = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            rotated[j][n-i-1] = table[i][j]

    return rotated            
            

    
    
    
