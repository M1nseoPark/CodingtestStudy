answer = 0

def solution(numbers, target):
    global answer
    
    def dfs(rst, d):
        global answer
        
        if d == len(numbers):
            if rst == target:
                answer += 1
            return
        
        dfs(rst + numbers[d], d + 1)
        dfs(rst - numbers[d], d + 1)
    
    dfs(0, 0)
    
    return answer
