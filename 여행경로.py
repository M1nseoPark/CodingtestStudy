from collections import deque

def solution(tickets):
    visited = [0 for _ in range(len(tickets))]
    n = (len(tickets) * 2 - 2) // 2 + 2
    
    q = deque()
    q.append(['ICN', 1])
    tickets.sort()
    answer = ['ICN']
    
    while q:
        here, v = q.popleft()
        
        if v == n:
            break
        
        for i in range(len(tickets)):
            if (tickets[i][0] == here) and (visited[i] == 0):
                q.append([tickets[i][1], v+1])
                answer.append(tickets[i][1])
                visited[i] = 1
                break
    
    return answer

print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
