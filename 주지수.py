import sys

n, m = map(int, sys.stdin.readline().split())
people = []
for _ in range(n):
    temp = list(map(int, sys.stdin.readline().split()))
    for i in range(1, m):
        temp[i] += temp[i-1]
        
    people.append(temp)

for i in range(m):
    for j in range(1, n):
        people[j][i] += people[j-1][i]


k = int(sys.stdin.readline())
for _ in range(k):
    # x가 행의 개수, 인덱스 1부터 시작 
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    x1 -= 1
    y1 -= 1
    x2 -= 1
    y2 -= 1

    if x1 >= 1 and y1 >= 1:
        answer = people[x2][y2] - people[x1-1][y2] - people[x2][y1-1] + people[x1-1][y1-1]
    elif x1 >= 1:
        answer = people[x2][y2] - people[x1-1][y2]
    elif y1 >= 1:
        answer = people[x2][y2] - people[x2][y1-1]
    else:
        answer = people[x2][y2]
        
    print(answer)

        
    
    
