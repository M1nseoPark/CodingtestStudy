def solution(scores):
    answer = 1

    yanho = scores[0]
    scores.sort(key=lambda x: (-x[0], x[1]))

    temp = 0
    for i in range(len(scores)):
        if yanho[0] < scores[i][0] and yanho[1] < scores[i][1]:
            return -1

        # 이렇게 하면 인센티브를 받지 못하는 사람은 아예 세지 않음 
        if temp <= scores[i][1]:
            # 완호보다 점수가 더 큰 사람이 있으면 완호의 등수가 내려감 
            if sum(yanho) < scores[i][0] + scores[i][1]:
                answer += 1
            temp = scores[i][1]
            
    return answer
