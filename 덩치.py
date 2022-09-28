n = int(input())
body = []
for _ in range(n):
    body.append(list(map(int, input().split())))

answer = [1 for _ in range(n)]

for i in range(n):
    for j in range(n):
        if i != j:
            if body[i][0] < body[j][0] and body[i][1] < body[j][1]:
                answer[i] += 1

for i in answer:
    print(i, end=' ')
