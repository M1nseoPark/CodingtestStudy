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


'''
내가 푼 이분탐색 풀이 -> python 시간 초과, pypy로 제출해야 함(중복된 temp 값도 계산하니까 그런가?)
import sys

n = int(sys.stdin.readline())
arr = []
for _ in range(n):
    arr.append(int(sys.stdin.readline()))

arr.sort()
answer = 0

for i in range(n-1, -1, -1):
    for j in range(i+1):
        temp = arr[i] - arr[j]
        left = j
        right = i
        while left <= right:
            rst = arr[left] + arr[right]
            if rst == temp:
                answer = max(arr[i], answer)
                break

            elif rst > temp:
                right -= 1

            else:
                left += 1

print(answer)
'''
