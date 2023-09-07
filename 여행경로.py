# DFS 풀이 
def solution(tickets):
    answer = []
    visited = [False] * len(tickets)

    def dfs(start, path):
        if len(path) == len(tickets) + 1:
            answer.append(path)
            return

        for idx, ticket in enumerate(tickets):
            if start == ticket[0] and visited[idx] = False:
                visited[idx] = True
                dfs(ticket[1], path+[ticket[1]])
                visited[idx] = False

    dfs('ICN', ['ICN'])
    answer.sort()

    return answer[0]


# BFS 풀이 
from collections import deque

def solution(tickets):
    answer = []
    q = deque()
    q.append(['ICN', ['ICN'], []])
    
    while q:
        now, path, visited = q.popleft()
        
        if len(visited) == len(tickets):
            answer.append(path)
        
        for idx, ticket in enumerate(tickets):
            if now == ticket[0] and idx not in visited:
                visited.append(idx)
                path.append(ticket[1])
                q.append([ticket[1], path[:], visited[:]])
                visited.pop()
                path.pop()
    
    answer.sort()
    return answer[0]
