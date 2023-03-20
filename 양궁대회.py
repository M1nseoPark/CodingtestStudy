import copy

def solution(n, info):
    global before, answer
    answer = [-1]
    before = 0
    
    def dfs(idx, cnt, arr):
        global answer, before
        
        if cnt == 0:
            score, peach = 0, 0
            for i in range(11):
                if info[i] >= arr[i] and info[i] != 0:
                    peach += 10 - i
                elif info[i] < arr[i]:
                    score += 10 - i
                    
            if score > peach and (score - peach) > before:
                before = score - peach
                answer = copy.deepcopy(arr)
            return
        
        if idx > 10:
            return
        
        for i in range(cnt, -1, -1):
            arr[10-idx] += i
            dfs(idx+1, cnt-i, arr)
            arr[10-idx] -= i
    
    dfs(0, n, [0]*11)
    return answer
