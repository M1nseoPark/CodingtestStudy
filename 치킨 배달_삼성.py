# 치킨집의 개수 최대 M개 -> 개수가 정해지지 않았는데 코드를 어떻게 짜지?
# 조합으로 풀기엔 너무 경우의 수가 많아질 것 같음..
## 진짜 combinations을 썼다고??? -> 파이썬 한정 쉬운 문제인듯

from itertools import combinations


n, m = map(int, input().split())
city = []
for _ in range(n):
    city.append(list(map(int, input().split())))


house = []
chicken = []
for i in range(n):
    for j in range(n):
        if city[i][j] == 1:
            house.append([i, j])

        if city[i][j] == 2:
            chicken.append([i, j])

num = 1
answer = []
while num <= m:
    pick = list(combinations(chicken, num))
    
    for k in range(len(pick)):
        result = 0
        for i in range(len(house)):
            temp = []
            for j in range(num):
                temp.append(abs(pick[k][j][0] - house[i][0]) + abs(pick[k][j][1] - house[i][1]))

            result += min(temp)
            
        answer.append(result)

    num += 1

print(min(answer))    


    


    
    
        
