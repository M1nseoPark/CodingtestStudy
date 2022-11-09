k, n = map(int, input().split())
line = []
for _ in range(k):
    line.append(int(input()))

left = 1   # 랜선의 길이는 1부터 시작 -> ZeroDivisionError
right = max(line)

while left <= right:
    mid = (left + right) // 2

    temp = 0
    for i in range(k):
        temp += (line[i] // mid)

    if temp >= n:
        left = mid + 1
    else:
        right = mid - 1


print(right)

'''
left right temp -> 정답으로 수렴
1 400 5
201 400 11
201 299 6
201 249 8
201 224 10
201 211 10
201 205 10
201 202 10
201 200 10
'''
