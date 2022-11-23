n = int(input())
arr = []
for _ in range(n):
    a, b, c, d = map(int, input().split())
    ## 3월 1일보다 빨리 지거나 11월 30일 보다 늦게 피는 꽃들은 리스트에 포함하지 않음
    # 날짜를 세자리 정수로 바꾸기!
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


'''
내가 푼 코드 
import sys

n = int(sys.stdin.readline())
flower = []
for _ in range(n):
    flower.append(list(map(int, sys.stdin.readline().split())))

flower.sort()
pick = []
start = []
s = 0
for i in range(n):
  if flower[i][0] < 3 or (flower[i][0] == 3 and flower[i][1] == 1):
    if len(start) == 0 or (start[2] < flower[i][2] or (start[2] == flower[i][2] and start[3] < flower[i][3])):
        start = flower[i]
        s = i

answer = 0

if len(start) == 0:
    answer = 0

else:
    pick.append(start)

    while True:
        if pick[-1][2] == 12:
            answer = len(pick)
            break
    
        if s == n - 1:
            answer = 0
            break
    
        temp = []
        for i in range(s+1, n):
            if pick[-1][2] > flower[i][0] or (pick[-1][2] == flower[i][0] and pick[-1][3] >= flower[i][1]):
                if len(temp) == 0 or (temp[2] < flower[i][2] or (temp[2] == flower[i][2] and temp[3] < flower[i][3])):
                    temp = flower[i]
                    s = i
    
        if len(temp) == 0:
            break
        else:
            pick.append(temp)

print(answer)
'''
