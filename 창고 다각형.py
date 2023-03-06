n = int(input())
pole = []
maxh, idx = 0, 0

for i in range(n):
    l, h = map(int, input().split())
    pole.append([l, h])
    
    if h > maxh:
        maxh = h
        idx = i

pole.sort()

temp = pole[0][1]  # 초기 높이는 첫번째 기둥의 높이
answer = maxh

# 최대 높이 전까지 돌면서 다음 기둥이 현재보다 높으면
# 현재의 면적을 계산해서 더해주고 높이를 다음 기둥으로 갱신
for i in range(idx):
    if temp < pole[i+1][1]:
        answer += temp * (pole[i+1][0] - pole[i][0])
        temp = pole[i+1][1]
    else:   # 아니면 그냥 현재 면적을 더해줌 
        answer += temp * (pole[i+1][0] - pole[i][0])
        
temp = pole[-1][1]
for i in range(n-1, idx, -1):
    if temp < pole[i-1][1]:
        answer += temp * (pole[i][0] - pole[i-1][0])
        temp = pole[i-1][1]
    else:  
        answer += temp * (pole[i][0] - pole[i-1][0])

print(answer)
    



    

    

    

    
    
