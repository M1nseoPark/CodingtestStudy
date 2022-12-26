def solution(genres, plays):
    divide = {}
    music = {}
    answer = []
    for i in range(len(genres)):
        if genres[i] not in divide:
            divide[genres[i]] = plays[i]
            music[genres[i]] = [[plays[i], -i]]
        else:
            divide[genres[i]] += plays[i]
            music[genres[i]].append([plays[i], -i])
    
    # 많이 재생된 장르부터 나열하기
    pick = []
    divide = sorted(divide.items(), key=lambda x: x[1], reverse=True)
    for i in range(len(divide)):
        pick.append(divide[i][0])
    
    # 가장 많이 재생된 두 장르에서 가장 많이 재생된 노래 구하기
    for i in pick:
        music[i].sort(reverse=True)
        for j in range(min(len(music[i]), 2)):
            answer.append(-music[i][j][1])
            
    return answer
