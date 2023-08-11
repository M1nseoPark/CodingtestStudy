from collections import deque

def solution(priorities, location):
    answer = 1
    q = deque(priorities)
    
    while len(q) > 1:
        cur = q.popleft()
        
        if cur < max(q):
            q.append(cur)
            if location == 0:
                location = len(q) - 1
            else:
                location -= 1
        else:
            if location == 0:
                return answer
            else:
                answer += 1
                location -= 1
        
        #print(q, location, answer)
            
    return answer

#solution([1, 1, 1, 2], 2)