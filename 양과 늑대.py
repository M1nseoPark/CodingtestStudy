## 내 오답 코드 
def solution(info, edges):
    global answer
    answer = 0
    n = len(info)
    adj = [[0] * n for _ in range(n)]
    sheep = set()
    
    for i in range(n):
        if info[i] == 0:
            sheep.add(i)
    
    for a, b in edges:
        adj[a][b] = 1
        adj[b][a] = 1
    
    
    def dfs(visited, idx, scnt, wcnt):   # 방문한 노드, 현재 인덱스, 양의 수, 늑대의 수
        global answer
        
        if sheep.issubset(visited):
            return
        
        answer = max(answer, scnt)
        
        for i in range(n):
            if adj[idx][i] == 1:
                if i not in visited:
                    visited.add(i)

                    if info[i] == 0:  # 양이라면 
                        dfs(visited, i, scnt+1, wcnt)
                    else:   # 늑대라면 
                        if scnt > wcnt+1:
                            dfs(visited, i, scnt, wcnt+1)

                    visited.remove(i)
                else:
                    dfs(visited, i, scnt, wcnt)
    
    dfs(set(), 0, 1, 0)
    return answer


## 정답 코드
def solution(info, edges):
    visited = [0] * len(info)
    answer = []

    def dfs(sheep, wolf):
        if sheep > wolf:
            answer.append(sheep)
        else:
            return
        
        for a, b in edges:
            if visited[a] and not visited[b]:
                visited[b] = 1
                if info[b] == 0:
                    dfs(sheep+1, wolf)
                else:
                    dfs(sheep, wolf+1)
                visited[b] = 0

    visited[0] = 1
    dfs(1, 0)

    return max(answer)