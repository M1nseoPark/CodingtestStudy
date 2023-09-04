from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(p):
    start = []

    # 응시자들의 위치 미리 큐에 담아주기 
    for i in range(5):
        for j in range(5):
            if p[i][j] == 'P':
                start.append([i, j])

    for s in start:
        q = deque([s])
        dist = [[-1] * 5 for i in range(5)]
        dist[s[0]][s[1]] = 0

        while q:
            y, x = q.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < 5 and 0 <= ny < 5 and dist[ny][nx] == -1:
                    if p[ny][nx] == 'O':
                        q.append([ny, nx])
                        dist[ny][nx] = dist[y][x] + 1

                    # 응시자와 가장 가까이 앉아 있는 응시자만 검사하면 됨 
                    if p[ny][nx] == 'P' and dist[y][x] <= 1:
                        return 0

    return 1
            
    
def solution(places):
    answer = []

    for i in places:
        answer.append(bfs(i))

    return answer

    return answer
