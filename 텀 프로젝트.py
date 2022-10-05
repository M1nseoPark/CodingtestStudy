from collections import deque
import sys

test = int(sys.stdin.readline())

def bfs(v):
    q = deque()
    q.append(v)
    visited[v] = True
    
    team = []
    team.append(v)

    while q:
        here = q.popleft()
        pick = student[here]

        if here == pick:
            group[here] = True
            
        elif v == pick:
            for i in range(len(team)):
                group[team[i]] = True

        elif pick in team:
            for i in range(team.index(pick), len(team)):
                group[team[i]] = True

        if not visited[pick]:
            q.append(pick)
            team.append(pick)
            visited[pick] = True
        
    
    
for _ in range(test):
    n = int(sys.stdin.readline())
    student = [0]
    student += list(map(int, sys.stdin.readline().split()))

    group = [False for i in range(n+1)]
    visited = [False for i in range(n+1)]

    for i in range(1, n+1):
        if not visited[i]:
            bfs(i)

    answer = 0
    for i in range(1, n+1):
        if not group[i]:
            answer += 1

    print(answer)

    

    

    
