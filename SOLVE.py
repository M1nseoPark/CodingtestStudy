n, l = map(int, input().split())
maps = []
for _ in range(n):
    maps.append(list(map(int, input().split())))

answer = 0

# 가로 줄
visited = [False for _ in range(n)]
for i in range(n):
    flag = True
    h, c = maps[i][0], 1
    for j in range(1, n):
        if h == maps[i][j]:
            c += 1
        else:
            if maps[i][j] - h == 1:
                if c >= l:
                    c = 1
                    h = maps[i][j]
                else:
                    flag = False
                    break
            else:
                flag = False
                break

    if flag:
        print(i)
        visited[i] = True
        answer += 1

    flag = True
    h, c = maps[i][n-1], 1
    for j in range(n-2, -1, -1):
        if h == maps[i][j]:
            c += 1
        else:
            if maps[i][j] - h == 1:
                if c >= l:
                    c = 1
                    h = maps[i][j]
                else:
                    flag = False
                    break
            else:
                flag = False
                break

    if flag and not visited[i]:
        print(i)
        answer += 1

print('-----')
        

# 세로 줄
visited = [False for _ in range(n)]
for j in range(n):
    flag = True
    h, c = maps[0][j], 1
    for i in range(1, n):
        if h == maps[i][j]:
            c += 1
        else:
            if maps[i][j] - h == 1:
                if c >= l:
                    c = 1
                    h = maps[i][j]
                else:
                    flag = False
                    break
            else:
                flag = False
                break

    if flag:
        print(j)
        visited[j] = True
        answer += 1

    flag = True
    h, c = maps[n-1][j], 1
    for i in range(n-2, -1, -1):
        if h == maps[i][j]:
            c += 1
        else:
            if maps[i][j] - h == 1:
                if c >= l:
                    c = 1
                    h = maps[i][j]
                else:
                    flag = False
                    break
            else:
                flag = False
                break

    if flag and not visited[j]:
        print(j)
        answer += 1


print(answer)
        
        
