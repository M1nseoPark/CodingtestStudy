n = int(input())
arr = []
for _ in range(n):
    a, b, c, d = map(int, input().split())
    ## 3월 1일보다 빨리 지거나 11월 30일 보다 늦게 피는 꽃들은 리스트에 포함하지 않음
    if 100*c+d < 301 or 100*a+b > 1130: continue
    arr.append([100*a+b, 100*c+d])

arr.sort()
flower = [-1, -1]
idx = -1
for i in range(n):
    ## 정렬했기 때문에 이후에는 3월 1일 이전에 핀 꽃이 없음
    if arr[i][0] > 301:
        break
    ## 3월 1일 이전에 핀 꽃 중에서 가장 늦게 진 꽃 구하기
    if arr[i][1] > flower[1]:
        flower = arr[i]
        idx = i
        
answer = 1
day = flower[1]  # 꽃이 진 날짜
while day <= 1130:
    nflower = [-1, -1]
    for i in range(idx, n): # 한 번도 확인하지 않은 인덱스부터
        if arr[i][0] > day:  # 마지막에 꽃이 진 날짜보다 다음 꽃이 늦게 피면
            break
        if flower[0] < arr[i][0] <= flower[1] < arr[i][1]:
            if arr[i][1] > nflower[1]:
                nflower = arr[i]
                idx = i

    if nflower[0] == -1:
        answer = 0
        break

    flower = nflower
    day = flower[1]
    answer += 1

print(answer)
