# 걍 이해가 안됨ㅠㅠㅠ

n, k = map(int, input().split())
thing = [[0, 0]]
for _ in range(n):
    thing.append(list(map(int, input().split())))

answer = [[0] * (k + 1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, k+1):
        w = thing[i][0]
        v = thing[i][1]

        if j < w:
            answer[i][j] = answer[i-1][j]  # 이전 물건, 같은 무게의 가치
        else:
            # max(물건을 넣어줬을 때 가치, 안넣었을 때 가치)
            answer[i][j] = max(v + answer[i-1][j-w], answer[i-1][j])
            print(v + answer[i-1][j-w], answer[i-1][j])
        print('------')

print(answer)
print(answer[n][k])
