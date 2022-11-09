# 조합 사용하면 메모리 초과
# x+y+z = k => x+y = k-z

n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))

arr.sort()
result = set()
for i in range(n):
    for j in range(n):
        result.add(arr[i]+arr[j])

answer = -1
for i in range(n-1, -1, -1):
    for j in range(i+1):
        if arr[i]-arr[j] in result:
            answer = arr[i]
            break

    if answer != -1:
        break

print(answer)

