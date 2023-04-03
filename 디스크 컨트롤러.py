import heapq

def solution(jobs):
    answer, now, i = 0, 0, 0   # now는 현재 시점 
    start = -1   # 바로 이전에 완료한 작업의 시작 시간 
    minHeap = []

    while i < len(jobs):
        for j in jobs:
            # 현재 시점에서 처리할 수 있는 작업이라면
            # 바로 이전에 완료한 작업의 시작 시간 < 작업 요청시간 <= 현재 시점 
            if start < j[0] <= now:   
                heapq.heappush(minHeap, [j[1], j[0]])

            # 처리할 수 있는 작업이 존재하면 
            if len(minHeap) > 0:
                cur = heapq.heappop(minHeap)
                start = now
                now += cur[0]
                answer += (now - cur[1])
                i += 1
            else:
                now += 1

    return answer // len(jobs)
                
                
