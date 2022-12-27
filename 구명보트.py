from collections import deque

def solution(people, limit):
    people.sort(reverse=True)
    people = deque(people)
    answer = 0
    
    while len(people) >= 2:
        if people[0] + people[-1] <= limit:
            people.pop()
        people.popleft()
        answer += 1
    
    if len(people) == 1:
        answer += 1
        
    return answer
