import heapq

def solution(n, k, enemy):
    maxHeap = []
    total, answer = 0, 0

    for i in range(len(enemy)):
        total += enemy[i]   # i라운드까지 총 적의 수 
        if total <= n:
            heapq.heappush(maxHeap, -enemy[i])
            answer += 1
        elif k > 0:   # 적의 수가 병사의 수보다 많을 경우
            k -= 1
            heapq.heappush(maxHeap, -enemy[i])
            total += heapq.heappop(maxHeap)
            answer += 1
        else:
            break

    return answer
            
            
            
            
            
    
