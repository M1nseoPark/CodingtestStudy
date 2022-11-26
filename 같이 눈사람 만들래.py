# 세 용액 문제는 3개를 고르는 거라 1중 for문으로 한개만 고정시켰는데
# 이 문제는 4개를 고르는 거라 2중 for문으로 두개를 고정시킴 

import sys


n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

arr.sort()
answer = max(arr)

for i in range(n):
    for j in range(i+3, n):
        left, right = i+1, j-1

        while left < right:
            temp = (arr[i] + arr[j]) - (arr[left] + arr[right])
            if abs(answer) > abs(temp):
                answer = abs(temp)

            if temp < 0:
                right -= 1

            else:
                left += 1

print(answer)
                

