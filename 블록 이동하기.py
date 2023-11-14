from collections import deque

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def solution(board):
    n = len(board)
    
    def can_move(cur1, cur2):
        temp = []
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]

        # 평행이동 
        for i in range(4):
            next1 = (cur1[0] + dy[i], cur1[1] + dx[i])
            next2 = (cur2[0] + dy[i], cur2[1] + dx[i])

            if 0 > next1[0] or 0 > next1[1] or next1[0] >= n or next1[1] >= n:
                continue

            if 0 > next2[0] or 0 > next2[1] or next2[0] >= n or next2[1] >= n:
                continue

            if board[next1[0]][next1[1]] == 0 and board[next2[0]][next2[1]] == 0:
                temp.append((next1, next2))
        
        # 회전 
        if cur1[0] == cur2[0]:  # 가로방향일 때 
            for d in [-1, 1]:  # up, down
                if 0 > cur1[0]+d or 0 > cur1[1] or cur1[0]+d >= n or cur1[1] >= n:
                    continue

                if 0 > cur2[0]+d or 0 > cur2[1] or cur2[0]+d >= n or cur2[1] >= n:
                    continue

                if board[cur1[0]+d][cur1[1]] == 0 and board[cur2[0]+d][cur2[1]] == 0:  # 회전 방향 대각선 칸, 회전하려는 칸
                    temp.append((cur1, (cur1[0]+d, cur1[1])))  # 상좌/하좌로 회전 
                    temp.append((cur2, (cur2[0]+d, cur2[1])))  # 상우/하우로 회전 

        else:  # 세로방향일 때 
            for d in [-1, 1]:  # left, right
                if 0 > cur1[0] or 0 > cur1[1]+d or cur1[0] >= n or cur1[1]+d >= n:
                    continue

                if 0 > cur2[0] or 0 > cur2[1]+d or cur2[0] >= n or cur2[1]+d >= n:
                    continue

                if board[cur1[0]][cur1[1]+d] == 0 and board[cur2[0]][cur2[1]+d] == 0:
                    temp.append(((cur1[0], cur1[1]+d), cur1))
                    temp.append(((cur2[0], cur2[1]+d), cur2))
        
        return temp

    
    q = deque([((0, 0), (0, 1), 0)])
    visited = set([((0, 0), (0, 1))])

    while q:
        cur1, cur2, cnt = q.popleft()
        if cur1 == (n-1, n-1) or cur2 == (n-1, n-1):
            return cnt
        
        for next in can_move(cur1, cur2):
            if next not in visited:
                q.append((next[0], next[1], cnt+1))
                visited.add(next)
        