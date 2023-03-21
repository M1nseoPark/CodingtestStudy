def solution(n, t, m, timetable):
    answer = 0
    crew = []
    for i in range(len(timetable)):
        ht, mt = timetable[i].split(':')
        crew.append(int(ht)*60+int(mt))
    crew.sort()

    bus = []
    for i in range(n-1):
        time = bus[-1][0] + t
        bus.append([time, 0])

    idx = 0   # 다음에 버스에 오를 크루의 인덱스
    for i in bus:
        cnt = 0   # 버스에 타는 크루의 수
        while cnt < m and i < len(crew) and crew[i] <= i:
            i += 1
            cnt += 1

        # 버스에 자리가 남았을 경우
        if cnt < m:
            answer = i
        else:   # 버스에 자리가 없는 경우 마지막 크루보다 1분 먼저 도착
            answer = crew[i-1] - 1

    return str(answer//60).zfill(2) + ":" + str(answer%60).zfill(2)
            
