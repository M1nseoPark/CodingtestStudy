import sys

t = int(input())
for _ in range(t):
    n, m = map(int, sys.stdin.readline().split())
    a = list(map(int, sys.stdin.readline().split()))
    b = list(map(int, sys.stdin.readline().split()))

    b.sort()
    answer = 0

    for i in range(n):
        for j in range(m):
            if a[i] <= b[j]:
                break
            else:
                answer += 1

    print(answer)


'''
arr = []
for i in range(n):
    arr.append([a[i], 0])

for i in range(m):
    arr.append([b[i], 1])

arr.sort()

cnt = 0
for i in range(n+m):
    if arr[i][1] == 0:
        anwer += cnt
    else:
        cnt += 1
'''


    
