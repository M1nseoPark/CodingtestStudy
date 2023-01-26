n, k = map(int, input().split())
medal = []
for _ in range(n):
    medal.append(list(map(int, input().split())))

medal.sort(key=lambda x:(x[1], x[2], x[3], x[0]), reverse=True)

answer = {}
idx, d = 1, 1
for i in range(n):
    if i == 0:
        answer[medal[i][0]] = idx
    elif medal[i-1][1] == medal[i][1] and medal[i-1][2] == medal[i][2] and medal[i-1][3] == medal[i][3]:
        answer[medal[i][0]] = idx
        d += 1
    else:
        idx += d
        d = 1
        answer[medal[i][0]] = idx

print(answer)
print(answer[k])
