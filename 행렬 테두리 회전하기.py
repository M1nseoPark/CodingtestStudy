dy = [1, 0, -1, 0]   # 동남서북 
dx = [0, 1, 0, -1]

# 행렬 인덱스 1부터 시작 
def solution(rows, columns, queries):
    answer = []
    arr = [[0] * columns for _ in range(rows)]
    idx = 1
    for i in range(rows):
        for j in range(columns):
            arr[i][j] = idx
            idx += 1
    
    def rotate(sx, sy, ex, ey):
        x, y, d = sx, sy, 0
        rst = []
        save = arr[x][y]
        
        while d != 4:
            nx = x + dx[d]
            ny = y + dy[d]
            
            if sx > nx or sy > ny or ex < nx or ey < ny:
                d += 1
                continue

            rst.append(save)
            arr[nx][ny], save = save, arr[nx][ny]
            x, y = nx, ny
        
        return min(rst)
            
    
    for i in range(len(queries)):
        x1, y1, x2, y2 = queries[i]
        answer.append(rotate(x1-1, y1-1, x2-1, y2-1))
        
    return answer


