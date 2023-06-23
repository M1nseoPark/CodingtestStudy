n = int(input())
A = list(map(int, input().split()))

answer = [-1] * n

for i in range(n):
    for j in range(i+1, n):
        if A[i] < A[j]:
            answer[i] = A[j]
            break

print(' '.join(map(str, answer)))
