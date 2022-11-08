a, b = map(int, input().split())

arr = []
i = 1
idx = 1
while len(arr) < b:
    arr += [idx] * i
    i += 1
    idx += 1

answer = 0
for i in range(a-1, b):
    answer += arr[i]

print(answer)
    
