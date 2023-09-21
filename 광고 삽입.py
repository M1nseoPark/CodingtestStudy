def change(time):
    time = list(map(int, time.split(':')))
    result = time[0] * 3600 + time[1] * 60 + time[2]
    return result


def solution(play_time, adv_time, logs):
    play = change(play_time)
    adv = change(adv_time)

    dp = [0] * (play + 1)

    for i in range(len(logs)):
        temp = list(logs[i].split('-'))
        start = change(temp[0])
        end = change(temp[1])
        dp[start] += 1
        dp[end] -= 1
    
    # 구간별 시청자 수 기록
    # [0, 0, 1, 0, 0, 0, -1, 0] -> [0, 0, 1, 1, 1, 1, 0, 0] 
    for i in range(1, play):
        dp[i] += dp[i-1]
    
    # 모든 구간 시청자 누적 기록 
    # [1, 1, 2, 2, 2, 2, 1] -> [1, 2, 3, 5, 7, 9, 11, 12]
    for i in range(1, play):
        dp[i] += dp[i-1]
    

    most_view = 0
    answer = 0
    for i in range(adv-1, play):
        if i >= adv:
            if most_view < dp[i] - dp[i-adv]:
                most_view = dp[i] - dp[i-adv]
                answer = i - adv + 1
        else:
            if most_view < dp[i]:
                most_view = dp[i]
                answer = i - adv + 1
    
    h, m, s = 0, 0, 0
    h = answer // 3600
    answer %= 3600
    m = answer // 60
    answer %= 60
    s = answer

    return h.zfill(2) + ':' + m.zfill(2) + ':' + s.zfill(2)

