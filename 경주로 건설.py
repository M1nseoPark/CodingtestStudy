import heapq

def solution(board):
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    n = len(board)
    
    minHeap = []
    heapq.heappush(minHeap, [0, 0, 0, -1])

    # 도착지점 중간 경로의 경우, 최솟값만 고려해주면 안되고 모든 경우를 고려해줘야 함 
    # (1, 2)가 목적지일 경우, (1, 1)을 (0, 1)로 거쳐가든지 (1, 0)으로 거쳐가든지 (1, 1)의 최소값은 같지만, 
    # (1, 2)는 (1, 0) -> (1, 1) -> (1, 2)가 빠르다
    dist = [[[500*n*n] * 2 for _ in range(n)] for _ in range(n)]   
    dist[0][0] = [0, 0]
    
    while minHeap:
        c, y, x, d = heapq.heappop(minHeap)
        
        if y == (n - 1) and x == (n - 1):
            break
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= ny < n and 0 <= nx < n and board[ny][nx] == 0:
                if d == -1 or d == i//2:  
                    cost = c + 100
                else:
                    cost = c + 600  # 코너가 필요한 경우 (코너길 1개+직선길 1개) 만들어야 함 
                
                if cost < dist[ny][nx][i//2]:
                    dist[ny][nx][i//2] = cost
                    heapq.heappush(minHeap, [cost, ny, nx, i//2])
    
    return min(dist[n-1][n-1])