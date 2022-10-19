import math

n, k = map(int, input().split())
student = [[0, 0] for _ in range(7)]

for i in range(n):
    s, y = map(int, input().split())
    student[y][s] += 1

answer = 0
for i in range(1, 7):
    answer += math.ceil(student[i][0] / k)
    answer += math.ceil(student[i][1] / k)

print(answer)
    
   



