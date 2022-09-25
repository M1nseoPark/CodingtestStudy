m, n = map(int, input().split())
box = []
for _ in range(n):
    box.append(list(map(int, input().split())))

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def bfs(y, x):
    q = []
    q.append([y, x])

    while q:
        y, x = q.pop(0)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n and box[ny][nx] == 0:
                box[ny][nx] = 1
                q.append([ny, nx])

answer = 0
for i in range(n):
    for j in range(m):
        if box[i][j] == 1:
            bfs(i, j)
            answer += 1

print(answer)
print(box)
            
            




        
    
    
    
    
        
    
    

    

            



        




    
