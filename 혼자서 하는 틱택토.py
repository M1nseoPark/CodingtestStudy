def isWin(board, y, x):
    l, r, t, d = (x - 1) % 3, (x + 1) % 3, (y - 1) % 3, (y + 1) % 3
    if board[y][x] == board[y][l] == board[y][r]:
        return True

    if board[y][x] == board[t][x] == board[d][x]:
        return True

    if (board[y][x] == board[t][l] == board[d][r]) or (board[y][x] == board[t][r] == board[d][l]):
        return True

    return False


def solution(board):
    oList, xList = [], []
    for i in range(3):
        for j in range(3):
            if board[i][j] == 'O':
                oList.append([i, j])
            elif board[i][j] == 'X':
                xList.append([i, j])

    if len(oList) < len(xList) or len(oList) - len(xList) > 1:
        return 0

    for i, j in oList:
        if isWin(board, i, j) and (len(xList) + 1) != len(oList):
            return 0

    for i, j in xList:
        if isWin(board, i, j) and len(xList) != len(oList):
            return 0

    return 1
