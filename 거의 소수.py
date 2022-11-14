# 메모리초과 문제

a, b = map(int, input().split())

arr = [True for _ in range(b+1)]
arr[0] = 0
arr[1] = 0

for i in range(2, int(b**0.5)+1):
    if arr[i]:
        for j in range(i+i, b+1, i):
            arr[j] = 0
            

answer = 0
for i in range(a, b+1):
    if arr[i] == 2:
        answer += 1

print(answer)
    
