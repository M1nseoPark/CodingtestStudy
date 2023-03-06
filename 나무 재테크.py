import sys

n, m, k = map(int, sys.stdin.readline().split())
A = []
for _ in range(n):
    A.append(list(map(int, sys.stdin.readline().split())))

nutri = [[5 for _ in range(n)] for _ in range(n)]  # 처음 양분은 모든 칸에 5만큼 있음
tree = [[deque() for _ in range(n)] for _ in range(n)]
for _ in range(m):
    x, y, z = map(int, sys.stdin.readline().split())
    tree[x-1][y-1].append(z)

dy = [-1, 0, 1, -1, 1, -1, 0, 1]
dx = [-1, -1, -1, 0, 0, 1, 1, 1]

year = 0
while year < k:
    ## 봄 + 여름
    # 입력으로 주어지는 나무 위치는 모두 다름 + 새로 생기는 나무는 리스트 왼쪽에 추가
    # -> 나이 어린 나무부터 정렬할 필요 없음 
    for i in range(n):
        for j in range(n):
            tlen = len(tree[i][j])
            for k in range(tlen):
                if tree[i][j][k] <= nutri[i][j]:
                    nutri[i][j] -= tree[i][j][k]  # 자신의 나이만큼 양분 먹음
                    tree[i][j][k] += 1  # 나이 1 증가
                else:
                    for _ in range(k, tlen):  # 뒤의 나무는 나이가 큰 나무들이니 무조건 죽음 
                        nutri[i][j] += tree[i][j].pop() // 2
                    break
                

    ## 가을
    for i in range(n):
        for j in range(n):
            for z in tree[i][j]:
                if z % 5 == 0:
                    for l in range(8):
                        nx = i + dx[l]
                        ny = j + dy[l]
                        if 0 <= nx < n and 0 <= ny < n:
                            tree[nx][ny].appendleft(1)

            # 겨울 
            tree[i][j] += A[i][j]

    year += 1


answer = 0
for i in range(len(tree)):
    if tree[i][2] != 0:
        answer += 1

print(answer)

    
