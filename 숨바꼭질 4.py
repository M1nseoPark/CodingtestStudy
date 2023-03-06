from collections import deque

n, k = map(int, input().split())

q = deque()
q.append(n)
visited = [-1] * 100001
visited[n] = 0
prev = [0] * 100001

while q:
    here = q.popleft()

    if here == k:
        break

    for i in [here*2, here-1, here+1]:
        if 0 <= i <= 100000 and visited[i] == -1:
            q.append(i)
            visited[i] = visited[here] + 1
            prev[i] = here

ans = [k]
while ans[-1] != n:
    ans.append(prev[ans[-1]])

print(visited[k])
print(' '.join(map(str, ans[::-1])))
    
