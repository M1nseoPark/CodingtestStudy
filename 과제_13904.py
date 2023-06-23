import sys

n = int(input())
arr = []
visited = [False] * 1001

for _ in range(n):
    arr.append(list(map(int, input().split())))

arr.sort(key=lambda x: x[1], reverse=True)
answer = 0

for d, w in arr:
    i = d
    while i > 0 and visited[i]:
        i -= 1

    if i == 0:
        continue
    else:
        visited[i] = True
        answer += w

print(answer)
            
    



