import sys
sys.setrecursionlimit(10000) 

def solution(n, m, sy, sx, r, c, k):
    global answer
    answer = ''
    dy = [1, 0, 0, -1]
    dx = [0, -1, 1, 0]
    code = ['d', 'l', 'r', 'u']
    
    dist = abs(sy - r) + abs(sx - c)
    if dist > k or (k - dist) % 2 == 1:
        return 'impossible'
    
    def dfs(y, x, route):
        global answer
        if answer != '':
            return
        
        if k < len(route) + abs(y - r) + abs(x - c):
            return
        
        if y == r and x == c and len(route) == k:
            answer = route
            return
        
        if len(route) >= k:
            return
        
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            
            if 0 < ny <= n and 0 < nx <= m:
                dfs(ny, nx, route+code[i])
        
    dfs(sy, sx, '')
    if answer == '':
        return 'impossible'
    
    return answer