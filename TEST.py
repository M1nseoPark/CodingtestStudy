def solution(elements):
    answer = set()
    n = len(elements)
    
    def dfs(idx, rst, cnt):
        if cnt > n:
            return
        
        rst += elements[idx]
        answer.add(rst)
        dfs((idx + 1) % n, rst, cnt + 1)
    
    for i in range(n):
        dfs(i, 0, 1)
            
    return len(answer)

print(solution([i for i in range(1, 1002)]))
        
    

        
    
    
