n = int(input())
arr = []
for _ in range(n):
    arr.append(list(input()))


def compress(y, x, s):
    global answer
    finish = True

    for i in range(y, y+s):
        for j in range(x, x+s):
            if arr[y][x] != arr[i][j]:
                finish = False
                break

        if not finish:
            break

    if finish:
        answer += arr[y][x]

    else:
        s = s // 2
        answer += '('
        
        compress(y, x, s)
        compress(y, x+s, s)
        compress(y+s, x, s)
        compress(y+s, x+s, s)
        answer += ')'


answer = ''
compress(0, 0, n)
print(answer)
