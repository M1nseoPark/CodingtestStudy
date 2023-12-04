def solution(stones, k):
    answer = 0
    left, right = 1, 200000000
    
    while left <= right:
        mid = (left + right) // 2
        cnt = 0
        
        for s in stones:
            if s - mid < 0:
                cnt += 1
            else:
                cnt = 0
            
            if cnt >= k:
                break
        
        if cnt < k:
            answer = mid
            left = mid + 1
        else:
            right = mid - 1
        
    return answer