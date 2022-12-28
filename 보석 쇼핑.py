def solution(gems):
    left, right = 0, 0
    m = len(set(gems))
    n = len(gems)
    result = n
    answer = [0, 0]
    
    visited = {}
    visited[gems[0]] = 1
    
    while left <= right:
        if len(visited) == m or right >= n:
            if len(visited) == m and result > right - left + 1:
                answer = [left+1, right+1]
                result = right - left + 1
            
            if gems[left] in visited:
                del visited[gems[left]]
            left += 1
        
        else:
            right += 1
            if right < n:
                visited[gems[right]] = 1
        
        print(visited)
        print(answer)
        print(left, right)
        print('------')
    
    return answer

solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"])
