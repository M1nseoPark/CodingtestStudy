import copy

n, m = map(int, input().split())
room = []
for _ in range(n):
    room.append(list(map(int, input().split())))

mode = [[0], [[0], [1], [2], [3]], [[1, 3], [0, 2]],
        [[0, 1], [1, 2], [2, 3], [0, 3]],
        [[0, 1, 3], [0, 1, 2], [1, 2, 3], [0, 2, 3]],
        [[0, 1, 2, 3]]]
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

cctv = []
for i in range(n):
    for j in range(m):
        if room[i][j] != 0 and room[i][j] != 6:
            cctv.append([i, j, room[i][j]])

def bfs(arr):
    temp = copy.deepcopy(room)
    cnt = 0
    
    for i in range(len(arr)):
        y, x, z, mm = arr[i]
        for j in mm:
            ny, nx = y, x
            while True:
                ny += dy[j]
                nx += dx[j]
                if ny < 0 or nx < 0 or ny >= n or nx >= m:
                    break

                if temp[ny][nx] == 6:
                    break

                if temp[ny][nx] == 0:
                    temp[ny][nx] = z

    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                cnt += 1

    return cnt
            
                
def dfs(idx, arr):
    global answer
    
    if idx == len(cctv):
        answer = min(answer, bfs(arr))
        return

    y, x, z = cctv[idx]
    for i in range(len(mode[z])):
        arr.append([y, x, z, mode[z][i]])
        dfs(idx+1, arr)
        arr.pop()

        
answer = float('inf')
dfs(0, [])
print(answer)
        
            
