n = int(input())
paper = []
for _ in range(n):
    paper.append(list(map(int, input().split())))


def cut(y, x, s):
    global white, blue
    finish = True

    for i in range(y, y+s):
        for j in range(x, x+s):
            if paper[y][x] != paper[i][j]:
                finish = False
                break

        if not finish:
            break


    if finish:
        if paper[y][x] == 0:
            white += 1
        else:
            blue += 1

    else:
        s = s // 2

        cut(y, x, s)
        cut(y, x+s, s)
        cut(y+s, x, s)
        cut(y+s, x+s, s)


white, blue = 0, 0
cut(0, 0, n)
print(white)
print(blue)
