import copy

n, m = map(int, input().split())
office = []
cctv = []
for i in range(n):
    office.append(list(map(int, input().split())))
    for j in range(m):
        if office[i][j] in [1, 2, 3, 4, 5]:
            cctv.append([office[i][j], i, j])

mode = [[], [[0], [1], [2], [3]],
        [[0, 2], [1, 3]],
        [[0, 3], [0, 1], [1, 2], [2, 3]],
        [[0, 2, 3], [0, 1, 3], [0, 1, 2], [1, 2, 3]],
        [[0, 1, 2, 3]]]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

answer = n * m


def fill(arr, mm, y, x):
    for h in mm:
        nx = x
        ny = y

        while True:
            nx += dx[h]
            ny += dy[h]
            # 부등호 잘못 써서 한참 헤맴!!
            if 0 > nx or 0 > ny or nx >= m or ny >= n:
                break

            if arr[ny][nx] == 6:
                break

            if arr[ny][nx] == 0:
                arr[ny][nx] = 7

    return arr


def dfs(depth, arr):
    global answer, n, m

    if depth == len(cctv):
        count = 0
        # 사각지대 개수 세기
        for i in range(n):
            for j in range(m):
                if arr[i][j] == 0:
                    count += 1

        answer = min(answer, count)
        return

    else:
        temp = copy.deepcopy(arr)
        num, y, x = cctv[depth]

        for i in mode[num]:
            temp = fill(temp, i, y, x)
            dfs(depth + 1, temp)
            temp = copy.deepcopy(arr)


dfs(0, office)
print(answer)
        
            
