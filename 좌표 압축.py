import bisect

n = int(input())
arr = list(map(int, input().split()))

new = sorted(list(set(arr)))
answer = []
for i in range(n):
    answer.append(bisect.bisect_left(new, arr[i]))

print(' '.join(map(str, answer)))
    
