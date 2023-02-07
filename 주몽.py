import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

answer = 0
for i in range(n):
    for j in range(i+1, n):
        if arr[i] + arr[j] == m:
            answer += 1

print(answer)
            
