n = int(input())
arr = {}
for i in range(1, n+1):
    arr[i] = int(input())

visited = [False] * (n + 1)
answer = 0

for k, v in arr.items():
    if k == v and not visited[v]:
        answer += 1
        visited[v] = True

    elif v in arr and arr[v] == k and not visited[v]:
        answer += 2
        visited[v] = True
        visited[k] = True

print(answer)
for i in range(1, n+1):
    if visited[i]:
        print(i)

