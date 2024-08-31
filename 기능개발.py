def solution(progresses, speeds):
    answer = []
    day = 0
    finish = 0
    
    while len(progresses) > 0:
        if (progresses[0] + speeds[0] * day) >= 100:
            finish += 1
            progresses.pop(0)
            speeds.pop(0)
        else:
            if finish > 0:
                answer.append(finish)
                finish = 0
            else:
                day += 1
    
    answer.append(finish)
    
    return answer