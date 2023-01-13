import sys

n, m, k = map(int, sys.stdin.readline().split())
A = []
for _ in range(n):
    A.append(list(map(int, sys.stdin.readline().split())))

nutri = [[5 for _ in range(n)] for _ in range(n)]  # 처음 양분은 모든 칸에 5만큼 있음
tree = {}
idx = 1
for _ in range(m):
    x, y, z = map(int, sys.stdin.readline().split())
    tree[idx] = [x-1, y-1, z]
    idx += 1

dy = [-1, 0, 1, -1, 1, -1, 0, 1]
dx = [-1, -1, -1, 0, 0, 1, 1, 1]

year = 0
while year < k:
    die = []   # 죽은 나무 
    
    ## 봄
    tree.sort(key=lambda x:x[2])  # 나이가 어린 나무부터
    for i in range(len(tree)):
        x, y, age = tree[i][0], tree[i][1], tree[i][2]
        if age != 0:
            if age <= nutri[x][y]:
                nutri[x][y] -= age  # 자신의 나이만큼 양분 먹음
                tree[i][2] += 1  # 나이 1 증가
            else:   # 먹지 못하면 바로 죽음
                tree[i][2] = 0  
                die.append([x, y, age])


    ## 여름
    for i in range(len(die)):
        x, y, age = die[i][0], die[i][1], die[i][2]
        nutri[x][y] += (age // 2)


    ## 가을
    for i in range(len(tree)):
        x, y, age = tree[i][0], tree[i][1], tree[i][2]
        if age != 0 and age % 5 == 0:  # 나이가 5의 배수인 나무의
            for j in range(8):
                nx = x + dx[j]
                ny = y + dy[j]

                if 0 <= nx < n and 0 <= ny < n:
                    tree.append([nx, ny, 1])  # 인접한 8개의 칸에 나이가 1인 나무 생김

    ## 겨울
    for i in range(n):
        for j in range(n):
            nutri[i][j] += A[i][j]   # 땅에 양분 A[r][c] 추가함


    year += 1


answer = 0
for i in range(len(tree)):
    if tree[i][2] != 0:
        answer += 1

print(answer)

    
