dy = [1, 0, -1, 0]
dx = [0, -1, 0, 1]

def solution(grid):
    answer = []
    n, m = len(grid), len(grid[0])

    visited = [[[False] * 4 for _ in range(m)] for _ in range(n)]

    for y in range(n):
        for x in range(m):
            for d in range(4):
                if visited[y][x][d]:
                    continue

                cnt = 0
                ny, nx = y, x
                while not visited[ny][nx][d]:
                    visited[ny][nx][d] = True
                    cnt += 1

                    if grid[ny][nx] == 'S':
                        pass
                    elif grid[ny][nx] == 'L':
                        d = (d - 1) % 4
                    else:
                        d = (d + 1) % 4

                    ny = (ny + dy[d]) % n
                    nx = (nx + dx[d]) % m

                answer.append(cnt)

    answer.sort()
    return answer
