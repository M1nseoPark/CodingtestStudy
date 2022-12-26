def solution(n, words):
    visited = {}
    idx = 1
    answer = [0, 0]
    
    for i in range(len(words)):
        if idx > n:
            idx = idx % n
        
        if i == 0:
            visited[words[i]] = 1
        else:
            if (words[i-1][-1] == words[i][0]) and (words[i] not in visited):
                visited[words[i]] = 1
            else:
                answer = [idx, i//n+1]
                break
        
        idx += 1 

    return answer
