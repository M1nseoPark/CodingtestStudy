p, m = map(int, input().split())
player = []
for _ in range(p):
    player.append(list(input().split()))

rooml = []
roomp = []
for i in range(p):
    if len(rooml) == 0:
        rooml.append([int(player[i][0])-10, int(player[i][0])+10])
        roomp.append([player[i]])

    else:
        flag = False
        for j in range(len(rooml)):
            if rooml[j][0] <= int(player[i][0]) <= rooml[j][1] and len(roomp[j]) < m:
                roomp[j].append(player[i])
                flag = True
                break

        if not flag:
            rooml.append([int(player[i][0])-10, int(player[i][0])+10])
            roomp.append([player[i]])
            

for i in range(len(roomp)):
    if len(roomp[i]) == m:
        print('Started!')
    else:
        print('Waiting!')

    roomp[i].sort(key=lambda x:x[1])

    for j in range(len(roomp[i])):
        print(' '.join(map(str, roomp[i][j])))

            
    
