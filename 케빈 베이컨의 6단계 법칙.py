# BFS로 풀었음

n, m = map(int, input().split())
friend = [[0] * (n + 1) for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    friend[a][b] = 1
    friend[b][a] = 1


def bfs(s, f):
    q = []
    q.append(s)
    visited = [0] * (n + 1)

    while q:
        here = q.pop(0)

        if here == f:
            break
        
        for i in range(1, n+1):
            if visited[i] == 0 and friend[here][i] == 1:
                visited[i] = visited[here] + 1
                q.append(i)

    return visited[here]           


answer = []
for i in range(1, n+1):
    result = 0
    for j in range(1, n+1):
        if i != j:
            result += bfs(i, j)
    answer.append([i, result])


kevin = [0, 5000]
for i in range(n):
    if kevin[1] > answer[i][1]:
        kevin[0] = i + 1
        kevin[1] = answer[i][1]

print(kevin[0])
        

'''
## 플로이드-워셜로도 풀어보기
for k in range(n):
    for i in range(n):
        for j in range(n):
            if i == j:
                friend[i][j] = 0   # 자기 자신과는 친구가 되지 못함
            else:
                friend[i][j] = min(friend[i][j], friend[i][k] + friend[k][j])
'''
