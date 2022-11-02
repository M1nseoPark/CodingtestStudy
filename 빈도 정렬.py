n, c = map(int, input().split())
arr = list(input().split())

count = {}
for i in range(n):
    if arr[i] in count:
        count[arr[i]] += 1
    else:
        count[arr[i]] = 1

count = sorted(count.items(), key=lambda x:x[1], reverse=True)

for i in range(len(count)):
    for j in range(count[i][1]):
        print(int(count[i][0]), end=' ')
