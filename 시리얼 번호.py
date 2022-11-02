n = int(input())
arr = []
for _ in range(n):
    s = input()
    t = 0
    for i in range(len(s)):
        if s[i] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            t += int(s[i])
    arr.append([s, len(s), t])

arr.sort(key=lambda x:(x[1], x[2], x[0]))

for i in range(n):
    print(arr[i][0])


