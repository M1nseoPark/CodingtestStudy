arr = list(input().split())
n = int(arr[0])
arr = arr[1:]

for i in range(len(arr)):
    arr[i] = int(arr[i][::-1])

while True:
    if len(arr) == n:
        break

    temp = list(input().split())
    for i in range(len(temp)):
        arr.append(int(temp[i][::-1]))

arr.sort()
for i in range(n):
    print(arr[i])
