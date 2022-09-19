n = int(input())
level = []
for _ in range(n):
    level.append(int(input()))

answer = 0
for i in range(n-2, -1, -1):
    if level[i+1] <= level[i]:
        temp = level[i]
        level[i] = level[i+1] - 1
        answer += (temp - level[i])

print(answer)
        
    
    
