from collections import deque

s = input()
t = input()

q = deque()
q.append(t)
visited = {}
visited[t] = 1

answer = 0
while q:
    here = q.popleft()

    if here == s:
        answer = 1
        break

    if len(here) >= 2 and (here[-1] == 'A') and (here[:-1] not in visited):
        q.append(here[:-1])
        visited[here[:-1]] = 1

    if len(here) >= 2 and (here[0] == 'B'):
        here = here[1:]
        if here[::-1] not in visited:
            q.append(here[::-1])
            visited[here[::-1]] = 1
        
print(answer)
