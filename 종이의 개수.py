n = int(input())
paper = []
for _ in range(n):
    paper.append(list(map(int, input().split())))

minus, zero, one = 0, 0, 0


def cut(y, x, s):
    global minus, zero, one
    finish = True
    
    for i in range(y, y+s):
        for j in range(x, x+s):
            if paper[y][x] != paper[i][j]:
                finish = False
                break

        if not finish:
            break
        

    if finish:
        if paper[y][x] == -1:
            minus += 1

        elif paper[y][x] == 0:
            zero += 1

        elif paper[y][x] == 1:
            one += 1

    else:
        s = s // 3
        cut(y, x, s)
        cut(y, x+s, s)
        cut(y, x+s*2, s)
        
        cut(y+s, x, s)
        cut(y+s, x+s, s)
        cut(y+s, x+s*2, s)

        cut(y+s*2, x, s)
        cut(y+s*2, x+s, s)
        cut(y+s*2, x+s*2, s)


cut(0, 0, n)
print(minus)
print(zero)
print(one)
            
        
                     
                     
