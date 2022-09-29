# 맞왜틀..
# DFS로도 풀 수 있다고 함!

n, m = map(int, input().split())
paper = []
for _ in range(n):
    paper.append(list(map(int, input().split())))

dx = [[0, 1, 0, 1],   # ㅁ
      # ㅡ
      [0, 1, 2, 3], [0, 0, 0, 0],
      # ㄴ
      [0, 0, 0, 1], [0, 0, 0, -1], [0, 0, 0, 1], [0, 0, 0, -1],
      [0, 0, 1, 2], [0, 0, -1, -2], [0, 1, 2, 0], [0, -1, -2, 0],
      # ㄹ
      [0, 0, 1, 1], [0, 0, -1, -1], [0, 1, 1, 2], [0, -1, -1, -2],
      # ㅜ
      [0, 1, 2, 1], [0, 1, 2, 1], [0, 0, 0, 1], [0, 0, 0, -1]]

dy = [[0, 0, 1, 1],   # ㅁ
      # ㅡ
      [0, 0, 0, 0], [0, 1, 2, 3],
      # ㄴ
      [0, 1, 2, 2], [0, 1, 2, 2], [0, 1, 2, 0], [0, 1, 2, 0],
      [0, 1, 1, 1], [0, 1, 1, 1], [0, 0, 0, 1], [0, 0, 0, 1],
      # ㄹ
      [0, 1, 1, 2], [0, 1, 1, 2], [0, 0, 1, 1], [0, 0, -1, -1],
      # ㅜ
      [0, 0, 0, 1], [0, 0, 0, -1], [0, 1, 2, 1], [0, 1, 2, 1]]


def put(y, x):
    # (y, x) 자리에 조각 한개씩 놓아봄
    for i in range(19):
        temp = 0
        for j in range(4):
            nx = x + dx[i][j]
            ny = y + dy[i][j]

            if 0 > nx or 0 > ny or m <= nx or n <= ny:
                temp = 0
                break
            else:
                temp += paper[ny][nx]

        if temp != 0:
            answer.append(temp)

            
answer = []    
for y in range(n):
    for x in range(m):
        put(y, x)

print(max(answer))
                
