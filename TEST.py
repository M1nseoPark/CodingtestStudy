from collections import deque


n, m = map(int, input().split())
maps = []
for _ in range(n):
    maps.append(list(map(int, input().split())))

cctv = [[0], [[[0, 1]], [[1, 0]], [[0, -1]], [[-1, 0]]],
        [[[0, -1], [0, 1]], [[1, 0], [-1, 0]]],
        [[[-1, 0], [0, 1]], [[0, 1], [1, 0]], [[1, 0], [0, -1]], [[0, -1], [-1, 0]]],
        [[[0, -1], [-1, 0], [0, 1]], [[-1, 0], [0, 1], [1, 0]], [[0, 1], [1, 0], [0, -1]], [[-1, 0], [1, 0], [0, -1]]],
        [[0, 1], [1, 0], [0, -1], [-1, 0]]]


site = []
for i in range(n):
    for j in range(m):
        if maps[i][j] != 0 and maps[i][j] != 6:
            site.append([maps[i][j], i, j])


def watch(arr, y, x):
    
            

    
for i in range(len(site)):
    t = site[i][0]
    for j in range(len(cctv[t])):
        watch(cctv[t][j], site[i][1], site[i][2])
    
    
