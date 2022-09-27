n, m = map(int, input().split())
city = []
for _ in range(n):
    city.append(list(map(int, input().split())))

# 좌표 -1
house = []
chicken = []
for i in range(n):
    for j in range(n):
        if city[i][j] == 1:
            house.append([i, j])

        if city[i][j] == 2:
            chicken.append([i, j])


distance = {}
result = []
for i in range(len(chicken)):
    t = []
    for j in range(len(house)):
        t.append(abs(chicken[i][0] - house[j][0]) + abs(chicken[i][1] - house[j][1]))

    distance[i] = t
    result.append([i, sum(distance[i])])

result.sort(key=lambda x:(x[1], x[0]), reverse=True)
print(distance)
print(result)

answer = []
while len(distance) > 0:
    num = 0

    for i in range(len(distance[0])):
        temp = 2*n
        k = distance.pop(result[0][0])
        for j in range(len(distance)):
            if distance[j][i] < temp:
                temp = distance[j][i]
                
        num += temp
            
    if len(distance) <= m:
        answer.append(num)
        
    del distance[result[0][0]]
    result.pop(0)

print(min(answer))
    


    
    
        
