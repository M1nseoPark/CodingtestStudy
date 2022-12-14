n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

temp = {}
for i in range(n):
    for j in range(n):
        t = arr[i][0] + arr[j][1]
        if len(temp) == 0 or t not in temp:
            temp[t] = 1
        else:
            temp[t] += 1
            

answer = 0
for i in range(n):
    for j in range(n):
        t = -1 * (arr[i][2] + arr[j][3])
        if t in temp:
            answer += temp[t]

print(answer)
    
