from collections import deque

n, k = map(int, input().split())

time, cnt = 1000000, 0
q = deque()
q.append([n, 0])
visited = [False] * 100001

while q:
    here, t = q.popleft()
    visited[here] = True   # 방문 처리를 여기서 해줌!

    if here == k:
        if time >= t:
            time = t
            cnt += 1
        else:
            break

    for i in [here*2, here-1, here+1]:
        if 0 <= i <= 100000 and not visited[i]:
            q.append([i, t+1])

print(time)
print(cnt)
