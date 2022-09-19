# 처음에 이중 for문으로 풀어서 계속 시간초과 뜸

import sys

n = int(sys.stdin.readline())
peak = list(map(int, sys.stdin.readline().split()))

answer = []
dragon = peak[0]
temp = 0
for i in range(1, n):
    if dragon > peak[i]:
        temp += 1
    else:
        answer.append(temp)
        dragon = peak[i]
        temp = 0
        
answer.append(temp)
print(max(answer))
