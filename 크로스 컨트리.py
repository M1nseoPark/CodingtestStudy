t = int(input())
for _ in range(t):
    n = int(input())
    count = {}   # 팀 당 주자 수
    temp = list(map(int, input().split()))

    for i in range(n):
        if temp[i] in count:
            count[temp[i]] += 1
        else:
            count[temp[i]] = 1

    dele = {}   # 제외되는 팀 
    for k, v in count.items():
        if v < 6:
            dele[k] = 1

    team = {}
    idx = 1
    for i in range(n):
        if temp[i] not in dele:
            if temp[i] in team:
                if team[temp[i]][0] < 4:
                    team[temp[i]][0] += 1
                    team[temp[i]][1] += idx
                elif team[temp[i]][0] == 4:
                    team[temp[i]][0] += 1
                    team[temp[i]][2] = idx
            else:
                team[temp[i]] = [1, idx, 0]

            idx += 1
            
    team = sorted(team.items(), key=lambda x:(x[1][1], x[1][2]))
    print(team[0][0])
        
            
        
