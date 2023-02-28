n = int(input())
parent = list(map(int, input().split()))
d = int(input())

def dfs(idx):
    parent[idx] = -2   # 노드 삭제 
    
    for i in range(n):
        if idx == parent[i]:   # 삭제된 노드가 부모노드인 노드 찾아 삭제 
            dfs(i)

dfs(d)
answer = 0
for i in range(n):
    if parent[i] != -2 and (i not in parent):   # 리프 노드여야 함
        answer += 1

print(answer)
            
