def solution(word):
    result = []
    arr = ['A', 'E', 'I', 'O', 'U']

    def dfs(cnt, w):
        if cnt == 5:
            return
        
        for i in range(5):
            result.append(w + arr[i])
            dfs(cnt + 1, w + arr[i])
    
    dfs(0, '')

    return result.index(word) + 1