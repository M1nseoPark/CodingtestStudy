n = int(input())
arr = list(map(int, input().split()))

location = [0 for _ in range(n+1)]
for i in range(1, n+1):
    location[arr[i]] = i

max_num = -1
count = 1

for i in range(1, n):
    if location[i] < location[i+1]:
        count += 1

        if count > max_num:
            max_num = max(max_num, count)

    else:
        count = 1


print(n - max_num)


    
