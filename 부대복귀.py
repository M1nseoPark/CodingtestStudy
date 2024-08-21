# 500 * (100,000 + 500,000) = 300,000,000
# 시간복잡도는 인접 행렬보다 인접 리스트를 사용하는 게 훨씬 유리하다!
from collections import deque, defaultdict

def solution(n, roads, sources, destination):
    adj = defaultdict(list)
    dic = {source: -1 for source in sources}
    
    # 인접 리스트 생성
    for a, b in roads:
        adj[a].append(b)
        adj[b].append(a)
    
    q = deque()
    q.append((destination, 0))
    visited = [False] * (n + 1)
    visited[destination] = True
    
    while q:
        here, cnt = q.popleft()
        
        if here in dic:
            dic[here] = cnt
        
        for next_node in adj[here]:
            if not visited[next_node]:
                visited[next_node] = True
                q.append((next_node, cnt + 1))
                    
    return list(dic.values())
