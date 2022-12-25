from collections import deque

def solution(begin, target, words):
    answer = 0
    q = deque()
    q.append([begin, 0])
    visited = {}
    
    while q:
        here, v = q.popleft()
        if here == target:
            answer = v
            break
        
        temp = []
        for i in words:
            d = 0
            for j in range(len(i)):
                if i[j] != here[j]:
                    d += 1
            if d == 1:
                temp.append(i)
        
        for i in range(len(temp)):
            if temp[i] not in visited:
                q.append([temp[i], v+1])
                visited[temp[i]] = 1
                
    return answer
