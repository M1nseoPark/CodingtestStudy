n, m, k = map(int, input().split())
sticker = []
for _ in range(k):
    r, c = map(int, input().split())
    temp = []
    for i in range(r):
        temp.append(list(map(int, input().split())))
    sticker.append(temp)


note = [[0] * m for _ in range(n)]
def check(y, x, d):
    r, c = len(sticker[d]), len(sticker[d][0])
    
    for i in range(r):
        for j in range(c):
            # 처음에 False 조건 잘못 설정해줌 -> 둘다 1일때만 불가능!!
            if note[y+i][x+j] == 1 and sticker[d][i][j] == 1:
                return False

    return True


def rotate(arr):
    r, c = len(arr), len(arr[0])

    result = [[0] * r for _ in range(c)]
    for i in range(r):
        for j in range(c):
            result[j][r-i-1] = arr[i][j]

    return result

    
def dfs(d, t):
    # 스티커를 다 붙이면 
    if d == k:
        answer = 0
        for i in range(n):
            for j in range(m):
                if note[i][j] == 1:
                    answer += 1

        print(answer)

    else:
        # 스티커를 붙일 수 있는 위치 찾기
        r, c = len(sticker[d]), len(sticker[d][0])
        flag = False
        
        for i in range(n-r+1):
            for j in range(m-c+1):
                if check(i, j, d):
                    # 스티커 붙이기 
                    for y in range(r):
                        for x in range(c):
                            if sticker[d][y][x] == 1:
                                note[y+i][x+j] = 1
                    flag = True
                    break

            if flag:
                break

        if flag:
            dfs(d+1, 0)
            
        # 스티커 회전 
        else:
            if t == 3:
                dfs(d+1, 0)
            else:
                sticker[d] = rotate(sticker[d])
                dfs(d, t+1)

dfs(0, 0)
    
