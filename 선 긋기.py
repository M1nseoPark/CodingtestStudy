import sys

n = int(sys.stdin.readline())
arr = []
for _ in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))

arr.sort()  # x가 작은 순서대로 주어진다는 말이 없었는데!
x, y = arr[0][0], arr[0][1]
answer = 0

for i in range(1, n):
    if arr[i][0] <= y:
        if arr[i][0] < x:
            x = arr[i][0]
        if arr[i][1] > y:
            y = arr[i][1]
        
    else:
        answer += (y - x)
        x = arr[i][0]
        y = arr[i][1]

        
answer += (y - x)
print(answer)
    
        
        
    
